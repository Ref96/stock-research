# Palmistry Skill for Claude Code

A complete palm reading skill integrating three classical systems: Cheiro (1916), D'Arpentigny (1843), and Nathaniel Altman's *Sexual Palmistry* (1986), plus notes from a witch family lineage.

## Installation

```bash
# From the repo root
cp -r skills/palmistry ~/.claude/skills/palmistry
```

Or install from the `.skill` bundle directly:

```bash
unzip palmistry.skill -d ~/.claude/skills/
```

After installing, run `autoskills` to update the skill index.

## Trigger Conditions

The skill activates automatically when you:

- Upload a palm photo and ask for a reading
- Say anything like "看手相", "read my hand", "what does this line mean"
- Mention any specific line — life line, head line, heart line, fate line, sun line
- Ask about hand shape, witch markers, compatibility, or sexual palmistry

Language is auto-detected; the reading is delivered in the same language you write in.

## What's Inside

| Section | Content |
|---|---|
| 0 | Reader ethics (witch family lineage rules; skip with "skip ethics") |
| 1 | Reading protocol — 11-step sequence, fixed order |
| 2 | Hand shape — Seven-type system (D'Arpentigny/Cheiro) + Four-element cross-check |
| 3 | Hand quality — consistency, flexibility, skin texture, temperature (Altman) |
| 4 | Thumb & four fingers — will, character, self-esteem, jealousy indicators |
| 5 | Eight mounts — including detailed Venus mount (key sexual indicator) |
| 6 | Five major lines — Head → Life → Heart → Fate → Sun |
| 7 | Minor lines & special marks — marriage lines, mystic cross, intuition line, etc. |
| 8 | Witch / psychic markers — 7-item checklist (天医线, 灵媒十字, 灵感圈, ...) |
| 9 | Time reading — dating events on each line by position |
| 10 | Reading style & voice principles |

### Reference Files

| File | Loaded when |
|---|---|
| `references/sexual.md` | User asks about love, relationships, compatibility, five types of lover |
| `references/special-marks.md` | Deep dive into minor lines, witch markers, special Cheiro signs |

## Key Principles

- **Head line is always read first** — it is the compass for interpreting every other line
- **Hand shape vs lines conflict** = internal tension; hand shape shows who you want to be, lines show who you've become
- **Never predict death** — absolute rule with both practical and metaphysical basis
- **Both hands** — non-dominant = inherited potential; dominant = current expression
- Negative indicators must be stated honestly; soften delivery, not content

## Sources

- Cheiro, *Palmistry for All* (1916) — primary system
- C.S. D'Arpentigny, *La Chirognomonie* (1843) — hand classification
- Nathaniel Altman, *Sexual Palmistry* (1986) — psychological and relational dimensions
- Practitioner notes from a witch family lineage (手相笔记.docx, 女巫掌.docx)
