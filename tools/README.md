# Personal Tools

Command-line utilities for personal use.

---

## organize_books_v2.py — 书籍智能分类脚本

Scans `~/Downloads` for book files and copies them into `~/Documents/书籍库/` sorted by a 14-category taxonomy. **Original files are never moved or deleted.**

### Supported Formats

`.pdf` `.epub` `.mobi` `.azw` `.azw3` `.djvu` `.cbz` `.cbr`

### Usage

```bash
# Preview mode (default) — shows what would be copied, nothing actually happens
python3 tools/organize_books_v2.py

# Execute — copies files into ~/Documents/书籍库/
python3 tools/organize_books_v2.py --run
```

Preview mode is always safe. Run it first to review the classification before committing.

After `--run`, a `分类报告.txt` is written to `~/Documents/书籍库/` listing every file and its assigned category.

### 14-Category Taxonomy

| # | Category | Examples |
|---|---|---|
| 01 | 拍卖·收藏 | Christie's, Sotheby's, Poly, Guardian catalogs |
| 02 | 手表·钟表 | Rolex, Patek, Breguet, horology, 陀飞轮 |
| 03 | 艺术·博物馆 | Met, Louvre, 故宫, art history, ceramics |
| 04 | 财经·投资 | Macro, stock, ETF, Buffett, 金融危机 |
| 05 | 商业·管理 | Management, startup, marketing, 品牌 |
| 06 | 中医·养生 | 黄帝内经, 本草, 针灸, TCM |
| 07 | 玄学·命理 | 八字, 紫微, 手相, 风水, tarot, astrology |
| 08 | 历史·文明 | 中国史, world history, 考古, 战争 |
| 09 | 传记·回忆录 | Biography, autobiography, memoir, 年谱 |
| 10 | 哲学·心理 | 论语, Kant, Freud, 认知, 决策 |
| 11 | 科学·技术 | Physics, AI, machine learning, 天文 |
| 12 | 文学·人文 | 红楼梦, fiction, poetry, linguistics |
| 13 | 旅行·地理 | Travel guide, atlas, 地图 |
| 14 | 其他·待分类 | Everything that doesn't match above |

Each major category has sub-folders (e.g., 02 splits into 品牌专著 / 机芯·技术 / 钟表史 / 收藏·鉴赏). Files that match only the top-level keyword land in the category root.

### Classification Logic

Matching is keyword-based against the filename (case-insensitive). Categories are evaluated top-to-bottom; the first match wins. Sub-category keywords are checked after the major category matches.

To adjust keywords or add categories, edit the `CATEGORIES` list in the script.

### Requirements

Python 3.9+ (uses `pathlib`, `shutil`, `os` from the standard library — no external packages needed).
