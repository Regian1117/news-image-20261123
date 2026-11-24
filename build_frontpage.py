"""Build and strictly verify the 1024x1024 Monday 23 November 2026 news frontpage."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Dict, List

from PIL import Image
from playwright.sync_api import sync_playwright

from data import (
    BRIEF_COL_A,
    BRIEF_COL_B,
    DATE_TITLE,
    EPISTEMIC_KEY,
    EXCLUSION_TEXT,
    HERO_STORIES,
    MID_STORIES,
    REGION_BY_ID,
    REGIONS,
    SOURCES_CREDIT,
    SUBHEAD,
    TAG_COLORS,
    TOP_META_LEFT,
    UTC_ANCHORS,
    BriefStory,
    FeatureStory,
    compute_region_counts,
    validate_dataset,
)
from svg_scenes import build_world_map_svg, get_scene


SVG_BG: Dict[int, str] = {
    1: "#EFF6FF",
    2: "#FFFBEB",
    3: "#F1F5F9",
    4: "#090F24",
    5: "#F1F5F9",
    6: "#FEF3C7",
    7: "#0C4A6E",
    8: "#166534",
    9: "#3B0764",
    10: "#1F2937",
    11: "#052E16",
    12: "#1C1917",
    13: "#450A0A",
}


def _render_hero_card(story: FeatureStory) -> str:
    reg_color = str(REGION_BY_ID[story.region]["color"])
    tag_color = TAG_COLORS[story.tag]
    _, scene_svg = get_scene(story.num)
    svg_bg = SVG_BG[story.num]
    return f"""
    <article class="hero-card" style="border-top: 3.5px solid {reg_color};">
      <div class="card-top">
        <div class="card-top-left">
          <span class="num-badge hero-badge" style="background:{reg_color};">{story.num}</span>
          <span class="kicker">{story.kicker}</span>
        </div>
        <span class="tag-pill" style="background:{tag_color};">{story.tag}</span>
      </div>
      <div class="hero-scene" style="background:{svg_bg};">{scene_svg}</div>
      <h2 class="hero-hl">{story.headline_html}</h2>
      <p class="hero-deck">{story.deck}</p>
      <div class="card-src">{story.source}</div>
    </article>"""


def _render_mid_card(story: FeatureStory) -> str:
    reg_color = str(REGION_BY_ID[story.region]["color"])
    tag_color = TAG_COLORS[story.tag]
    _, scene_svg = get_scene(story.num)
    svg_bg = SVG_BG[story.num]
    return f"""
    <article class="mid-card" style="border-top: 3px solid {reg_color};">
      <div class="mid-top">
        <span class="num-badge mid-badge" style="background:{reg_color};">{story.num}</span>
        <span class="mid-kicker">{story.kicker}</span>
      </div>
      <div class="mid-scene" style="background:{svg_bg};">{scene_svg}</div>
      <h3 class="mid-hl">{story.headline_html}</h3>
      <p class="mid-deck">{story.deck}</p>
      <div class="mid-foot">
        <span class="tag-pill mid-tag" style="background:{tag_color};">{story.tag}</span>
        <span class="mid-src">{story.source}</span>
      </div>
    </article>"""


def _render_brief_row(brief: BriefStory) -> str:
    reg_color = str(REGION_BY_ID[brief.region]["color"])
    pill = ""
    if brief.inline_tag:
        tag_color = TAG_COLORS[brief.tag]
        pill = f' <span class="inline-claim" style="background:{tag_color};">{brief.tag}</span>'
    return f"""
    <div class="b-row" data-num="{brief.num}">
      <span class="b-num" style="background:{reg_color};">{brief.num}</span>
      <span class="b-body"><strong class="b-subj">{brief.subject}</strong> {brief.text}{pill}</span>
      <span class="b-src">{brief.source}</span>
    </div>"""


def build_html() -> str:
    total_stories = validate_dataset()
    counts = compute_region_counts()

    region_chips = "".join(
        f'<span class="reg-chip" style="background:{r["color"]};">'
        f'{r["upper"]} <strong>{counts[str(r["id"])]}</strong></span>'
        for r in REGIONS
    )

    utc_items = '<span class="utc-div">|</span>'.join(
        f'<span class="utc-item">{anchor}</span>' for anchor in UTC_ANCHORS
    )

    hero_html = "".join(_render_hero_card(s) for s in HERO_STORIES)
    mid_html = "".join(_render_mid_card(s) for s in MID_STORIES)
    col_a_html = "".join(_render_brief_row(b) for b in BRIEF_COL_A)
    col_b_html = "".join(_render_brief_row(b) for b in BRIEF_COL_B)

    legend_html = "".join(
        f'<div class="leg-item"><span class="leg-dot" style="background:{r["color"]};"></span>'
        f'<span class="leg-lbl">{r["name"]} ({counts[str(r["id"])]})</span></div>'
        for r in REGIONS
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  html, body {{
    width: 1024px;
    height: 1024px;
    overflow: hidden;
    background: #FAF8F3;
    color: #0F172A;
    font-family: 'Segoe UI', Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  .page {{
    width: 1024px;
    height: 1024px;
    padding: 6px 12px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    overflow: hidden;
  }}

  /* Header */
  .hdr {{
    flex: 0 0 auto;
    border-bottom: 2.5px solid #0F172A;
    padding-bottom: 3px;
  }}
  .meta-row {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 9.8px;
    line-height: 1.15;
    letter-spacing: 0.45px;
    margin-bottom: 1px;
  }}
  .meta-left {{
    color: #991B1B;
    font-weight: 900;
    text-transform: uppercase;
  }}
  .meta-right {{
    color: #0F172A;
    font-weight: 800;
  }}
  .masthead {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 44px;
    font-weight: 700;
    line-height: 1.0;
    letter-spacing: -0.4px;
    text-align: center;
    color: #0F172A;
    margin: 0;
  }}
  .subhead {{
    font-size: 11.5px;
    font-weight: 800;
    color: #991B1B;
    text-align: center;
    line-height: 1.2;
    margin: 2px 0 3px;
  }}
  .reg-strip {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 4px;
  }}
  .reg-chip {{
    flex: 1 1 auto;
    text-align: center;
    color: #FFFFFF;
    font-size: 8.6px;
    font-weight: 800;
    letter-spacing: 0.25px;
    padding: 2px 4px;
    border-radius: 2px;
    white-space: nowrap;
  }}
  .reg-chip strong {{
    font-weight: 900;
    margin-left: 2px;
  }}

  /* Chronological UTC ribbon */
  .utc-bar {{
    flex: 0 0 auto;
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    border-radius: 3px;
    padding: 2.5px 6px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 4px;
    height: 22px;
  }}
  .utc-badge {{
    background: #B91C1C;
    color: #FFFFFF;
    font-size: 8.8px;
    font-weight: 900;
    letter-spacing: 0.4px;
    padding: 1.5px 5px;
    border-radius: 2px;
    white-space: nowrap;
  }}
  .utc-track {{
    flex: 1 1 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 9.8px;
    font-weight: 700;
    color: #0F172A;
    white-space: nowrap;
  }}
  .utc-div {{
    color: #94A3B8;
    font-weight: 400;
    padding: 0 2px;
  }}

  /* Shared badges & tags */
  .num-badge {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    color: #FFFFFF;
    font-weight: 900;
    flex-shrink: 0;
  }}
  .tag-pill {{
    color: #FFFFFF;
    font-size: 7.8px;
    font-weight: 900;
    letter-spacing: 0.35px;
    padding: 1.5px 4.5px;
    border-radius: 2px;
    white-space: nowrap;
    line-height: 1.1;
  }}
  .num-sans, .sans-num {{
    font-family: 'Segoe UI', Arial, sans-serif;
    font-weight: 900;
    letter-spacing: -0.2px;
  }}

  /* Top Tier: 3 Hero Cards (exact 212px) */
  .hero-tier {{
    flex: 0 0 212px;
    height: 212px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
  }}
  .hero-card {{
    background: #FFFFFF;
    border: 1px solid #C8BFAF;
    border-radius: 2px;
    padding: 4px 7px 4px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    height: 212px;
    overflow: hidden;
  }}
  .card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 4px;
    height: 18px;
    flex-shrink: 0;
  }}
  .card-top-left {{
    display: flex;
    align-items: center;
    gap: 5px;
    min-width: 0;
  }}
  .hero-badge {{
    width: 17px;
    height: 17px;
    font-size: 10px;
  }}
  .kicker {{
    font-size: 9.3px;
    font-weight: 900;
    color: #334155;
    letter-spacing: 0.3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .hero-scene {{
    width: 100%;
    height: 80px;
    flex: 0 0 80px;
    border-radius: 2px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .hero-scene svg {{
    display: block;
    width: 100%;
    height: 80px;
  }}
  .hero-hl {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 16px;
    font-weight: 700;
    line-height: 1.13;
    color: #020617;
    letter-spacing: -0.15px;
  }}
  .hero-hl .num-sans, .hero-hl .sans-num {{
    font-size: 15.2px;
  }}
  .hero-deck {{
    font-size: 11.2px;
    line-height: 1.22;
    color: #1E293B;
  }}
  .card-src {{
    margin-top: auto;
    font-size: 8.8px;
    font-weight: 700;
    color: #475569;
    line-height: 1.1;
    white-space: nowrap;
  }}

  /* Middle Tier: 10 Regional Feature Cards (exact 318px) */
  .mid-tier {{
    flex: 0 0 318px;
    height: 318px;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 6px;
  }}
  .mid-card {{
    background: #FFFFFF;
    border: 1px solid #C8BFAF;
    border-radius: 2px;
    padding: 2.5px 5.5px 2.5px;
    display: flex;
    flex-direction: column;
    gap: 1.5px;
    height: 156px;
    overflow: hidden;
  }}
  .mid-top {{
    display: flex;
    align-items: center;
    gap: 4px;
    height: 15px;
    flex-shrink: 0;
  }}
  .mid-badge {{
    width: 15px;
    height: 15px;
    font-size: 8.8px;
  }}
  .mid-kicker {{
    font-size: 8.3px;
    font-weight: 900;
    color: #334155;
    letter-spacing: 0.2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .mid-scene {{
    width: 100%;
    height: 46px;
    flex: 0 0 46px;
    border-radius: 2px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .mid-scene svg {{
    display: block;
    width: 100%;
    height: 46px;
  }}
  .mid-hl {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 12.2px;
    font-weight: 700;
    line-height: 1.09;
    color: #020617;
    letter-spacing: -0.1px;
  }}
  .mid-hl .num-sans, .mid-hl .sans-num {{
    font-size: 11.6px;
  }}
  .mid-deck {{
    font-size: 10.4px;
    line-height: 1.14;
    letter-spacing: 0.1px;
    color: #1E293B;
  }}
  .mid-foot {{
    margin-top: auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 4px;
    padding-top: 0;
    flex-shrink: 0;
  }}
  .mid-tag {{
    font-size: 7.4px;
    padding: 1px 4px;
  }}
  .mid-src {{
    font-size: 8.2px;
    font-weight: 700;
    color: #475569;
    white-space: nowrap;
  }}

  /* Lower Tier: Map + 22 Briefs */
  .lower-tier {{
    flex: 1 1 auto;
    min-height: 0;
    display: grid;
    grid-template-columns: 248px 1fr;
    gap: 7px;
  }}
  .panel {{
    background: #FFFFFF;
    border: 1px solid #C8BFAF;
    border-radius: 2px;
    padding: 5px 6px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    min-height: 0;
  }}
  .panel-hdr {{
    font-size: 9.2px;
    font-weight: 900;
    color: #0F172A;
    letter-spacing: 0.35px;
    border-bottom: 1.5px solid #0F172A;
    padding-bottom: 2.5px;
    margin-bottom: 4px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .map-wrap {{
    flex: 0 0 auto;
    width: 100%;
    aspect-ratio: 360 / 172;
    border: 1px solid #CBD5E1;
    border-radius: 2px;
    overflow: hidden;
    background: #D8EBF8;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .map-wrap svg {{
    width: 100%;
    height: 100%;
    display: block;
  }}
  .map-note {{
    flex: 0 0 auto;
    margin-top: 5px;
    padding: 3px 5px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 2px;
    font-size: 8.4px;
    font-weight: 700;
    color: #475569;
    line-height: 1.25;
  }}
  .map-legend {{
    flex: 1 1 auto;
    margin-top: 6px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    align-content: space-between;
    gap: 4px 6px;
  }}
  .leg-item {{
    display: flex;
    align-items: center;
    gap: 4px;
    min-width: 0;
  }}
  .leg-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }}
  .leg-lbl {{
    font-size: 8.6px;
    font-weight: 700;
    color: #1E293B;
    white-space: nowrap;
  }}

  /* 22 Briefs grid */
  .briefs-grid {{
    flex: 1 1 auto;
    min-height: 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
  }}
  .brief-col {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-width: 0;
  }}
  .brief-col:first-child {{
    border-right: 1px solid #E5DFD2;
    padding-right: 7px;
  }}
  .b-row {{
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 10.6px;
    line-height: 1.15;
    height: 19px;
    white-space: nowrap;
    border-bottom: 1px solid #F1EDE4;
    padding-bottom: 1px;
  }}
  .b-row:last-child {{
    border-bottom: none;
    padding-bottom: 0;
  }}
  .b-num {{
    width: 18px;
    height: 16px;
    border-radius: 2px;
    color: #FFFFFF;
    font-size: 9px;
    font-weight: 900;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .b-body {{
    flex: 1 1 auto;
    min-width: 0;
    color: #1E293B;
    letter-spacing: -0.18px;
    overflow: hidden;
    white-space: nowrap;
  }}
  .b-subj {{
    color: #0F172A;
    font-weight: 800;
  }}
  .inline-claim {{
    display: inline-block;
    color: #FFFFFF;
    font-size: 7.4px;
    font-weight: 900;
    padding: 0.5px 3.5px;
    border-radius: 2px;
    vertical-align: middle;
    letter-spacing: 0.2px;
  }}
  .b-src {{
    flex-shrink: 0;
    font-size: 8.4px;
    font-weight: 700;
    color: #475569;
    letter-spacing: -0.1px;
  }}

  /* Exclusion bar */
  .excl-bar {{
    flex: 0 0 auto;
    background: #FEF2F2;
    border: 1.2px solid #DC2626;
    border-radius: 2px;
    padding: 3px 7px;
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 9.2px;
    line-height: 1.22;
    color: #450A0A;
  }}
  .excl-badge {{
    background: #B91C1C;
    color: #FFFFFF;
    font-size: 8.2px;
    font-weight: 900;
    letter-spacing: 0.35px;
    padding: 2px 5px;
    border-radius: 2px;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .db-txt {{
    letter-spacing: 0.1px;
  }}

  /* Bottom footer */
  .footer {{
    flex: 0 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.3px;
    line-height: 1.15;
    color: #475569;
    padding: 0 1px;
    white-space: nowrap;
  }}
  .footer-left {{
    font-weight: 700;
    color: #334155;
  }}
  .footer-right {{
    font-weight: 600;
    color: #64748B;
  }}
</style>
</head>
<body>
  <main class="page">
    <header class="hdr">
      <div class="meta-row">
        <span class="meta-left">{TOP_META_LEFT}</span>
        <span class="meta-right">{total_stories} DATED STORIES · 9 REGIONS · 14 FIELDS · ALL FROM MON 23 NOV 2026</span>
      </div>
      <h1 class="masthead">{DATE_TITLE}</h1>
      <div class="subhead">{SUBHEAD}</div>
      <div class="reg-strip">{region_chips}</div>
    </header>

    <section class="utc-bar" aria-label="Chronological UTC ribbon">
      <span class="utc-badge">MONDAY UTC</span>
      <div class="utc-track">{utc_items}</div>
    </section>

    <section class="hero-tier" aria-label="Top stories">
      {hero_html}
    </section>

    <section class="mid-tier" aria-label="Regional features">
      {mid_html}
    </section>

    <section class="lower-tier" aria-label="Map and briefs">
      <div class="panel map-panel">
        <div class="panel-hdr">WHERE IT HAPPENED · SCENES 1–13</div>
        <div class="map-wrap">{build_world_map_svg()}</div>
        <div class="map-note">Pins 1–13 locate the illustrated lead &amp; feature stories; all 35 items color-coded across 9 regions below.</div>
        <div class="map-legend">{legend_html}</div>
      </div>
      <div class="panel briefs-panel">
        <div class="panel-hdr">ALSO ON MONDAY 23 NOVEMBER · 22 MORE DATED BRIEFS (9 REGIONS MATCHED BY COLOR)</div>
        <div class="briefs-grid">
          <div class="brief-col">{col_a_html}</div>
          <div class="brief-col">{col_b_html}</div>
        </div>
      </div>
    </section>

    <section class="excl-bar" aria-label="Date verification">
      <span class="excl-badge">DATE CHECK · EXCLUDED</span>
      <span class="excl-text db-txt">{EXCLUSION_TEXT}</span>
    </section>

    <footer class="footer">
      <span class="footer-left">{EPISTEMIC_KEY}</span>
      <span class="footer-right">{SOURCES_CREDIT}</span>
    </footer>
  </main>
</body>
</html>
"""


DOM_AUDIT_JS = """
() => {
  const errs = [];
  const doc = document.documentElement;
  if (doc.scrollWidth > 1024 || doc.scrollHeight > 1024) {
    errs.push(`Page scroll overflow: ${doc.scrollWidth}x${doc.scrollHeight}`);
  }
  const page = document.querySelector('.page');
  if (page.scrollWidth > 1024 || page.scrollHeight > 1024) {
    errs.push(`.page scroll overflow: ${page.scrollWidth}x${page.scrollHeight}`);
  }

  // Check section overlaps in .page
  const bands = Array.from(page.children);
  for (let i = 0; i < bands.length - 1; i++) {
    const r1 = bands[i].getBoundingClientRect();
    const r2 = bands[i + 1].getBoundingClientRect();
    if (r1.bottom > r2.top + 0.5) {
      errs.push(`Band overlap: ${bands[i].className} bottom=${r1.bottom.toFixed(1)} > ${bands[i+1].className} top=${r2.top.toFixed(1)}`);
    }
  }
  const lastBand = bands[bands.length - 1].getBoundingClientRect();
  if (lastBand.bottom > 1024.1) {
    errs.push(`Last band exceeds canvas: bottom=${lastBand.bottom.toFixed(1)}`);
  }

  // Check Hero & Mid cards and panels for scroll overflow & internal overlaps / footer clipping
  const checkContainer = (selector, footSel) => {
    document.querySelectorAll(selector).forEach((el, idx) => {
      if (el.scrollHeight > el.clientHeight + 1) {
        errs.push(`${selector}[${idx}] vertical overflow: scrollH=${el.scrollHeight} > clientH=${el.clientHeight}`);
      }
      if (el.scrollWidth > el.clientWidth + 1) {
        errs.push(`${selector}[${idx}] horizontal overflow: scrollW=${el.scrollWidth} > clientW=${el.clientWidth}`);
      }
      const box = el.getBoundingClientRect();
      const children = Array.from(el.children);
      for (let i = 0; i < children.length - 1; i++) {
        const a = children[i].getBoundingClientRect();
        const b = children[i + 1].getBoundingClientRect();
        if (a.bottom > b.top + 0.5) {
          errs.push(`${selector}[${idx}] child overlap: ${children[i].className} vs ${children[i+1].className}`);
        }
      }
      if (footSel) {
        const foot = el.querySelector(footSel);
        if (foot) {
          const fr = foot.getBoundingClientRect();
          if (fr.bottom > box.bottom + 0.5 || fr.right > box.right + 0.5) {
            errs.push(`${selector}[${idx}] ${footSel} clipped`);
          }
        }
      }
    });
  };
  checkContainer('.hero-card', '.card-src');
  checkContainer('.mid-card', '.mid-foot');
  checkContainer('.panel', null);

  // Check legend labels have no horizontal clipping
  document.querySelectorAll('.leg-lbl').forEach((lbl, idx) => {
    if (lbl.scrollWidth > lbl.clientWidth + 1) {
      errs.push(`.leg-lbl[${idx}] overflow: "${lbl.textContent}"`);
    }
  });

  // Check every .b-row height <= 20px and zero horizontal text clipping
  document.querySelectorAll('.b-row').forEach((row, idx) => {
    const r = row.getBoundingClientRect();
    if (r.height > 20.1) {
      errs.push(`.b-row[${idx}] height ${r.height.toFixed(1)} > 20px`);
    }
    const body = row.querySelector('.b-body');
    if (body && body.scrollWidth > body.clientWidth + 1) {
      errs.push(`.b-row[${idx}] text overflow: scrollW=${body.scrollWidth} > clientW=${body.clientWidth} ("${body.textContent.slice(0,30)}")`);
    }
  });

  // Check SVG text clipping and SVG pill padding >= 3px
  let globalMinPillPad = 999;
  document.querySelectorAll('svg').forEach((svg, sIdx) => {
    const sb = svg.getBoundingClientRect();
    svg.querySelectorAll('text').forEach((txt, tIdx) => {
      const tb = txt.getBoundingClientRect();
      if (tb.left < sb.left - 0.5 || tb.right > sb.right + 0.5 || tb.top < sb.top - 0.5 || tb.bottom > sb.bottom + 0.5) {
        errs.push(`SVG[${sIdx}] text[${tIdx}] "${txt.textContent}" clipped outside SVG`);
      }
    });
    svg.querySelectorAll('.svg-pill').forEach((pill, pIdx) => {
      const bg = pill.querySelector('.pill-bg');
      const txt = pill.querySelector('.pill-txt');
      if (bg && txt) {
        const br = bg.getBoundingClientRect();
        const tr = txt.getBoundingClientRect();
        const padL = tr.left - br.left;
        const padR = br.right - tr.right;
        const padT = tr.top - br.top;
        const padB = br.bottom - tr.bottom;
        const minPad = Math.min(padL, padR, padT, padB);
        if (minPad < globalMinPillPad) globalMinPillPad = minPad;
        if (minPad < 3.0) {
          errs.push(`SVG[${sIdx}] pill[${pIdx}] "${txt.textContent}" tight pad=${minPad.toFixed(2)}px (L:${padL.toFixed(1)} R:${padR.toFixed(1)} T:${padT.toFixed(1)} B:${padB.toFixed(1)})`);
        }
      }
    });
  });

  // Check map pin pairwise distances in viewBox coordinates (>= 20px)
  const pins = Array.from(document.querySelectorAll('#world-map .map-pin')).map(el => ({
    num: el.getAttribute('data-num'),
    x: parseFloat(el.getAttribute('data-x')),
    y: parseFloat(el.getAttribute('data-y')),
  }));
  const pinMap = Object.fromEntries(pins.map(p => [p.num, p]));
  const pDist = (a, b) => Number(Math.hypot(pinMap[a].x - pinMap[b].x, pinMap[a].y - pinMap[b].y).toFixed(1));
  let minDist = 9999;
  for (let i = 0; i < pins.length; i++) {
    for (let j = i + 1; j < pins.length; j++) {
      const d = Math.hypot(pins[i].x - pins[j].x, pins[i].y - pins[j].y);
      if (d < minDist) minDist = d;
      if (d < 20.0) {
        errs.push(`Map pin collision: #${pins[i].num} and #${pins[j].num} dist=${d.toFixed(1)} < 20`);
      }
    }
  }

  const b31 = document.querySelector('.b-row[data-num="31"]');
  const b31Body = b31 ? b31.querySelector('.b-body') : null;
  const brief31 = b31 && b31Body ? {
    height: Number(b31.getBoundingClientRect().height.toFixed(1)),
    singleLine: b31.getBoundingClientRect().height <= 20.1 && b31Body.scrollWidth <= b31Body.clientWidth + 1,
  } : null;

  return {
    errs,
    metrics: {
      pageW: doc.scrollWidth,
      pageH: doc.scrollHeight,
      heroCount: document.querySelectorAll('.hero-card').length,
      midCount: document.querySelectorAll('.mid-card').length,
      briefCount: document.querySelectorAll('.b-row').length,
      pinCount: pins.length,
      minPinDist: Number(minDist.toFixed(1)),
      pinSep_2_5_12: { '2-5': pDist('2', '5'), '2-12': pDist('2', '12'), '5-12': pDist('5', '12') },
      minPillPadPx: Number(globalMinPillPad.toFixed(2)),
      brief31,
      heroH: Math.round(document.querySelector('.hero-tier').getBoundingClientRect().height),
      midH: Math.round(document.querySelector('.mid-tier').getBoundingClientRect().height),
      lowerH: Math.round(document.querySelector('.lower-tier').getBoundingClientRect().height),
    }
  };
}
"""


def _launch_chromium(pw):
    for kwargs in ({}, {"channel": "msedge"}, {"channel": "chrome"}):
        try:
            return pw.chromium.launch(**kwargs)
        except Exception:
            continue
    return pw.chromium.launch()


def render_frontpage() -> None:
    repo_dir = Path(__file__).resolve().parent
    out_png = repo_dir / "entry.png"
    html = build_html()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        raw_png = tmp_path / "raw_entry.png"

        with sync_playwright() as pw:
            browser = _launch_chromium(pw)
            page = browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
            page.set_content(html, wait_until="load")
            page.evaluate("() => document.fonts ? document.fonts.ready : Promise.resolve()")
            audit: Dict[str, object] = page.evaluate(DOM_AUDIT_JS)
            page.screenshot(path=str(raw_png), full_page=False)
            browser.close()

        # Optimize PNG cleanly with Pillow
        with Image.open(raw_png) as img:
            assert img.size == (1024, 1024), f"Expected 1024x1024, got {img.size}"
            rgb = img.convert("RGB")
            rgb.save(out_png, format="PNG", optimize=True, compress_level=9)

            # Save 300x300 preview into OS temp folder (never inside repo)
            preview_path = Path(tempfile.gettempdir()) / "news_frontpage_preview_300.png"
            thumb = rgb.resize((300, 300), Image.Resampling.LANCZOS)
            thumb.save(preview_path, format="PNG", optimize=True)

    size_bytes = out_png.stat().st_size
    size_kib = size_bytes / 1024.0
    errs: List[str] = audit["errs"]  # type: ignore[assignment]
    metrics = audit["metrics"]

    print(f"DOM errs={errs}")
    print(f"Metrics={metrics}")
    print(f"entry.png={size_bytes} bytes ({size_kib:.1f} KiB)")
    print(f"300x300 preview={preview_path}")

    if errs:
        raise SystemExit(f"DOM audit failed with {len(errs)} error(s)")
    if size_kib > 250.0:
        raise SystemExit(f"entry.png too large: {size_kib:.1f} KiB > 250 KiB")


if __name__ == "__main__":
    render_frontpage()
