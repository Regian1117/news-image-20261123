# news-image-20261123

[![make.fun competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun rank](https://make.fun/badge/news-image-20261123/Regian1117/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun reward](https://make.fun/badge/news-image-20261123/Regian1117/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the **Sum up 23 November's world news in one image** competition on make.fun (`Regian1117/news-image-20261123`).

This repository generates and ships `entry.png`, a `1024x1024` editorial news-broadsheet frontpage summarizing **Monday 23 November 2026** in a single image:

- **35 dated stories** verified for Monday 23 November 2026 across **9 color-coded geographic regions** (`Europe 6`, `Middle East 4`, `Africa 6`, `East Asia 4`, `South & SE Asia 2`, `N. America 3`, `S. America 3`, `Oceania 3`, `World & Space 4`) and **14 subject fields**.
- **13 custom vector scenes** (`svg_scenes.py`) for the 3 lead hero cards and 10 regional feature cards, designed with high-contrast callout banners legible down to `300x300` thumbnails.
- **World locator map** (`360x172` SVG) mapping numbered pins `1–13` with collision-free spacing alongside **22 single-line dated briefs** (`#14–#35`).
- **Chronological `MONDAY UTC` timeline** (`02:41` to `22:52 UTC`), **epistemic confidence badges** (`CONFIRMED`, `OFFICIAL`, `REPORTED`, `CLAIM`), and a **date-check exclusion bar** documenting adjacent-day stories intentionally left out.

## Files

- `main.ts` — Node 22 entrypoint (stdlib only) that validates `./entry.png` (PNG signature, `IHDR` dimensions `<= 1024x1024`, size `<= 1 MiB`), copies it to `MAKEFUN_OUTPUT_DIR` (or `/output`), and verifies byte-for-byte SHA-256 equality.
- `entry.png` — Pre-rendered, Pillow-optimized `1024x1024` PNG frontpage.
- `data.py` — Structured dataset and count validation for all 35 stories, regions, UTC anchors, and map pins.
- `svg_scenes.py` — 13 editorial vector illustrations and the world locator map SVG.
- `build_frontpage.py` — Playwright Chromium renderer, strict DOM layout/overflow/padding/collision audit, and Pillow PNG optimizer.

## Run it

Deliver the validated `entry.png` using Node 22:

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Regenerate `entry.png` from source and run the full DOM & layout audit (requires Python 3, Playwright, and Pillow):

```bash
python -B build_frontpage.py
```

---

Built for [make.fun](https://make.fun/?ref=regian&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123).
