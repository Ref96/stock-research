#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
书籍智能分类脚本 v2（14大类体系）
扫描 ~/Downloads 中的所有书籍文件，按14大类复制到 ~/Documents/书籍库/
原文件不会被删除或移动，完全安全。
"""

import os
import shutil
from pathlib import Path

# ─────────────────────────────────────────────
# 配置区
# ─────────────────────────────────────────────

SOURCE_DIR = Path.home() / "Downloads"
OUTPUT_DIR = Path.home() / "Documents" / "书籍库"
BOOK_EXTENSIONS = {".pdf", ".epub", ".mobi", ".azw", ".azw3", ".djvu", ".cbz", ".cbr"}

# ─────────────────────────────────────────────
# 14大类分类规则
# 越靠前优先级越高
# ─────────────────────────────────────────────

CATEGORIES = [
    {
        "name": "01_拍卖·收藏",
        "sub": {
            "佳士得":   ["christie", "佳士得"],
            "苏富比":   ["sotheby", "苏富比"],
            "保利":     ["poly", "保利拍卖"],
            "嘉德":     ["guardian", "嘉德"],
            "西泠":     ["xiling", "西泠"],
            "其他拍行": ["bonham", "phillips", "nagel", "artcurial", "匡时", "华艺", "银座", "荣宝", "auction", "拍卖", "lot ", "catalogue", "catalog", "sale "],
        },
        "keywords": ["christie", "sotheby", "bonham", "phillips", "nagel", "artcurial",
                     "auction", "拍卖", "佳士得", "苏富比", "保利", "嘉德", "西泠",
                     "匡时", "华艺", "银座", "荣宝", "lot ", "catalogue", "catalog", "sale "],
    },
    {
        "name": "02_手表·钟表",
        "sub": {
            "品牌专著": ["rolex", "patek", "omega", "breguet", "jaeger", "vacheron",
                        "longines", "seiko", "iwc", "tudor", "cartier watch", "audemars",
                        "blancpain", "glashutte", "zenith", "tissot", "grand seiko"],
            "机芯·技术": ["movement", "calibre", "escapement", "机芯", "擒纵", "陀飞轮", "tourbillon", "complications"],
            "钟表史":   ["horology", "history of watch", "钟表史", "制表史"],
            "收藏·鉴赏": ["collecting watch", "vintage watch", "腕表收藏", "古董表", "怀表"],
            "图片参考": [],
        },
        "keywords": ["watch", "clock", "horology", "timepiece", "chronograph",
                     "手表", "钟表", "腕表", "怀表", "时计", "计时",
                     "rolex", "patek", "omega", "breguet", "jaeger", "vacheron",
                     "longines", "seiko", "cartier", "iwc", "tudor", "audemars",
                     "blancpain", "glashutte", "zenith", "tourbillon", "陀飞轮"],
    },
    {
        "name": "03_艺术·博物馆",
        "sub": {
            "大都会博物馆": ["metropolitan", "met museum", "大都会"],
            "其他博物馆":   ["british museum", "louvre", "guggenheim", "moma", "tate",
                            "大英博物馆", "卢浮宫", "故宫", "上海博物馆", "国家博物馆"],
            "艺术史":       ["art history", "艺术史", "美术史"],
            "画家·雕塑家":  ["picasso", "monet", "matisse", "rembrandt", "da vinci",
                            "齐白石", "张大千", "徐悲鸿", "黄宾虹"],
            "器物·古董":    ["ceramics", "porcelain", "jade", "bronze", "瓷器", "玉器",
                            "青铜", "书画", "古董", "文物", "器物"],
            "设计·工艺":    ["design", "craft", "bauhaus", "设计", "工艺", "装帧"],
        },
        "keywords": ["metropolitan", "met museum", "大都会", "british museum", "louvre",
                     "art history", "艺术史", "美术史", "museum", "博物馆", "exhibition",
                     "picasso", "monet", "齐白石", "张大千", "ceramics", "porcelain",
                     "瓷器", "玉器", "青铜", "书画", "古董", "文物", "design", "设计"],
    },
    {
        "name": "04_财经·投资",
        "sub": {
            "宏观经济":   ["macro", "gdp", "monetary", "inflation", "宏观经济", "货币政策",
                          "经济周期", "通胀", "美联储", "央行", "federal reserve"],
            "股票·证券":  ["stock", "equity", "technical analysis", "fundamental",
                          "炒股", "股票", "证券", "A股", "港股", "美股", "选股", "技术分析", "k线"],
            "基金·ETF":  ["fund", "etf", "index fund", "基金", "指数基金", "资产配置"],
            "房地产":     ["real estate", "reits", "property", "房地产", "楼市"],
            "另类投资":   ["alternative", "commodity", "crypto", "bitcoin", "大宗商品",
                          "加密货币", "比特币", "艺术品投资"],
            "价值投资":   ["value invest", "buffett", "munger", "graham", "巴菲特",
                          "芒格", "格雷厄姆", "价值投资", "security analysis"],
            "个人理财":   ["personal finance", "financial planning", "理财", "保险", "财务规划"],
            "金融史·危机":["financial crisis", "crash", "bubble", "金融危机", "泡沫",
                          "大萧条", "1929", "2008", "lehman"],
        },
        "keywords": ["macro", "gdp", "monetary", "inflation", "stock", "equity",
                     "fund", "etf", "real estate", "reits", "buffett", "munger",
                     "graham", "financial", "invest", "宏观经济", "货币政策", "炒股",
                     "股票", "证券", "基金", "房地产", "巴菲特", "价值投资", "理财",
                     "金融危机", "大宗商品", "加密货币", "财经"],
    },
    {
        "name": "05_商业·管理",
        "sub": {
            "企业管理":     ["management", "leadership", "strategy", "管理", "领导力", "战略"],
            "创业·商业模式":["startup", "entrepreneurship", "business model",
                            "创业", "商业模式", "venture"],
            "营销·品牌":    ["marketing", "branding", "consumer", "营销", "品牌", "消费者"],
            "企业史·案例":  ["company history", "corporate", "企业史", "公司传记", "商业案例"],
        },
        "keywords": ["management", "leadership", "strategy", "startup", "entrepreneurship",
                     "marketing", "branding", "corporate", "管理", "领导力", "战略",
                     "创业", "商业模式", "营销", "品牌", "企业史"],
    },
    {
        "name": "06_中医·养生",
        "sub": {
            "经典古籍": ["黄帝内经", "伤寒论", "金匮", "温病", "素问", "灵枢", "难经"],
            "本草·方剂": ["本草", "方剂", "汤头", "中药", "草药", "materia medica"],
            "针灸·穴位": ["针灸", "穴位", "经络", "acupuncture", "meridian"],
            "养生·食疗": ["养生", "食疗", "气功", "导引", "五行"],
            "现代中医":  ["中西医", "临床中医", "国医"],
        },
        "keywords": ["中医", "中药", "本草", "针灸", "经络", "黄帝内经", "伤寒",
                     "汤头", "方剂", "穴位", "脉经", "温病", "国医", "草药",
                     "tcm", "acupuncture", "养生", "食疗", "气功"],
    },
    {
        "name": "07_玄学·命理",
        "sub": {
            "易经·占卜":  ["易经", "周易", "六爻", "奇门", "梅花", "卜卦"],
            "四柱·紫微":  ["八字", "四柱", "紫微", "子平", "命理"],
            "风水·堪舆":  ["风水", "堪舆", "阳宅", "阴宅", "feng shui"],
            "相术·面相":  ["面相", "手相", "骨相", "相术", "palmistry", "physiognomy"],
            "西方玄学":   ["tarot", "astrology", "塔罗", "占星", "星盘",
                          "numerology", "kabbalah", "occult", "esoteric"],
        },
        "keywords": ["玄学", "风水", "八字", "紫微", "星盘", "占星", "塔罗",
                     "易经", "周易", "算命", "命理", "相术", "面相", "手相",
                     "奇门", "六爻", "四柱", "堪舆", "astrology", "tarot",
                     "numerology", "feng shui", "occult", "esoteric"],
    },
    {
        "name": "08_历史·文明",
        "sub": {
            "中国史":     ["中国史", "中国通史", "中华", "明史", "清史", "汉史", "唐史", "宋史"],
            "世界史":     ["world history", "european history", "世界史", "欧洲史",
                          "美洲史", "中东史", "非洲史"],
            "艺术史·考古":["考古", "文物研究", "archaeology", "发掘"],
            "军事·战争":  ["war", "military", "battle", "战争", "军事", "战役", "兵法", "孙子"],
            "文化·社会史":["cultural history", "social history", "文化史", "社会史",
                          "风俗", "宗教史"],
        },
        "keywords": ["历史", "史记", "通史", "断代史", "考古", "文物", "文明",
                     "朝代", "帝国", "战争", "history", "historical", "ancient",
                     "dynasty", "empire", "civilization", "archaeology",
                     "中国史", "世界史", "欧洲史", "军事", "战役"],
    },
    {
        "name": "09_传记·回忆录",
        "sub": {
            "艺术家·藏家": ["画家传", "collector", "藏家", "艺术家传"],
            "政治·历史人物":["emperor", "president", "politician", "帝王", "政治家"],
            "商界人物":     ["entrepreneur biography", "企业家", "投资人传记"],
            "学者·文人":    ["scholar", "philosopher", "文人", "学者", "作家传"],
        },
        "keywords": ["传记", "自传", "回忆录", "biography", "autobiography",
                     "memoir", "life of", "年谱", "日记"],
    },
    {
        "name": "10_哲学·心理",
        "sub": {
            "东方哲学": ["儒家", "道家", "佛学", "禅", "论语", "道德经", "confucius", "taoism", "buddhism"],
            "西方哲学": ["philosophy", "plato", "aristotle", "kant", "nietzsche",
                        "哲学", "存在主义", "古典哲学"],
            "心理学":   ["psychology", "psychotherapy", "freud", "jung", "cognitive",
                        "心理学", "认知", "行为心理", "心理治疗"],
            "思维·认知": ["thinking", "decision", "cognitive bias", "思维", "决策", "认知偏差"],
        },
        "keywords": ["philosophy", "psychology", "哲学", "心理", "儒家", "道家", "佛学",
                     "论语", "道德经", "plato", "kant", "freud", "jung",
                     "cognitive", "认知", "思维", "决策"],
    },
    {
        "name": "11_科学·技术",
        "sub": {
            "自然科学": ["physics", "chemistry", "biology", "astronomy",
                        "物理", "化学", "生物", "天文"],
            "科技·AI":  ["artificial intelligence", "machine learning", "technology",
                        "人工智能", "机器学习", "科技"],
            "科学史":   ["history of science", "科学史", "科学家传记"],
        },
        "keywords": ["physics", "chemistry", "biology", "astronomy", "science",
                     "artificial intelligence", "machine learning", "technology",
                     "物理", "化学", "生物", "天文", "科学", "人工智能", "科技"],
    },
    {
        "name": "12_文学·人文",
        "sub": {
            "中国文学": ["红楼梦", "水浒", "三国", "西游", "诗词", "唐诗", "宋词", "古文"],
            "外国文学": ["novel", "fiction", "literature", "小说", "外国文学"],
            "语言·文字": ["linguistics", "etymology", "训诂", "文字学", "语言学"],
        },
        "keywords": ["literature", "fiction", "novel", "poetry", "文学", "小说",
                     "诗词", "古文", "红楼", "语言", "文字", "linguistics"],
    },
    {
        "name": "13_旅行·地理",
        "sub": {
            "旅行指南": ["travel guide", "旅行", "旅游", "guidebook"],
            "地理·地图": ["geography", "atlas", "map", "地理", "地图", "地图册"],
        },
        "keywords": ["travel", "geography", "atlas", "旅行", "旅游", "地理", "地图"],
    },
]

UNCATEGORIZED_NAME = "14_其他·待分类"


# ─────────────────────────────────────────────
# 核心逻辑
# ─────────────────────────────────────────────

def classify_book(filename: str) -> tuple[str, str]:
    """
    返回 (大类文件夹名, 子类文件夹名)
    """
    name_lower = filename.lower()
    for cat in CATEGORIES:
        for kw in cat["keywords"]:
            if kw.lower() in name_lower:
                # 匹配到大类后，再判断子类
                sub_name = "通用"
                if "sub" in cat:
                    for sub_key, sub_kws in cat["sub"].items():
                        for skw in sub_kws:
                            if skw.lower() in name_lower:
                                sub_name = sub_key
                                break
                        if sub_name != "通用":
                            break
                return cat["name"], sub_name
    return UNCATEGORIZED_NAME, ""


def collect_books(source: Path) -> list[Path]:
    books = []
    for root, _, files in os.walk(source):
        for f in files:
            if Path(f).suffix.lower() in BOOK_EXTENSIONS:
                books.append(Path(root) / f)
    return books


def organize(dry_run: bool = False):
    print(f"\n{'='*60}")
    print(f"  书籍整理脚本 v2（14大类体系）")
    print(f"  来源：{SOURCE_DIR}")
    print(f"  输出：{OUTPUT_DIR}")
    print(f"  模式：{'【预览】不实际复制' if dry_run else '【执行】复制文件'}")
    print(f"{'='*60}\n")

    books = collect_books(SOURCE_DIR)
    if not books:
        print("⚠️  未找到书籍文件")
        return

    print(f"📚 共发现 {len(books)} 本书籍\n")

    stats = {}
    report_lines = []

    for book_path in sorted(books):
        cat_name, sub_name = classify_book(book_path.name)

        # 有子类就放子文件夹，没有就放大类根目录
        if sub_name and sub_name != "通用":
            dest_dir = OUTPUT_DIR / cat_name / sub_name
            label = f"{cat_name} / {sub_name}"
        else:
            dest_dir = OUTPUT_DIR / cat_name
            label = cat_name

        dest_path = dest_dir / book_path.name
        stats[cat_name] = stats.get(cat_name, 0) + 1
        report_lines.append(f"{label} | {book_path.name}")

        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
            if dest_path.exists():
                stem, suffix = book_path.stem, book_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
            shutil.copy2(book_path, dest_path)
            print(f"  ✅ {label:<35}  {book_path.name[:40]}")
        else:
            print(f"  🔍 {label:<35}  {book_path.name[:40]}")

    # 统计
    print(f"\n{'─'*60}")
    print("📊 各大类数量：")
    for k in sorted(stats):
        print(f"   {k}：{stats[k]} 本")
    print(f"   合计：{len(books)} 本")

    if not dry_run:
        report_path = OUTPUT_DIR / "分类报告.txt"
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("书籍分类报告（14大类体系）\n" + "="*60 + "\n")
            for line in sorted(report_lines):
                f.write(line + "\n")
        print(f"\n📄 报告：{report_path}")
        print(f"📁 结果：{OUTPUT_DIR}")

    print("\n✨ 完成！原始文件未被移动或删除。\n")


if __name__ == "__main__":
    import sys
    dry_run = "--run" not in sys.argv
    if dry_run:
        print("\n💡 预览模式 — 加 --run 参数才真正复制：")
        print("   python3 organize_books_v2.py --run\n")
    organize(dry_run=dry_run)
