"""Custom editorial vector scenes (1-13) and world map SVG for the frontpage."""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

from data import MAP_PINS, REGION_BY_ID

FONT_SANS = "'Segoe UI', Arial, sans-serif"


def _star_points(cx: float, cy: float, r_outer: float, r_inner: float) -> str:
    pts: List[str] = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        r = r_outer if i % 2 == 0 else r_inner
        pts.append(f"{cx + r * math.cos(ang):.1f},{cy + r * math.sin(ang):.1f}")
    return " ".join(pts)


def _banner(
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    fill: str,
    stroke: str = "#FFFFFF",
    stroke_w: float = 1.2,
    font_size: float = 13.5,
    text_fill: str = "#FFFFFF",
    rx: float = 4.0,
) -> str:
    cx = x + w / 2.0
    cy = y + h / 2.0
    return (
        f'<g class="svg-pill">'
        f'<rect class="pill-bg" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
        f'rx="{rx:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_w:.1f}"/>'
        f'<text class="pill-txt" x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" '
        f'dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" '
        f'font-size="{font_size:.1f}" fill="{text_fill}" letter-spacing="0.3">{text}</text>'
        f"</g>"
    )


def hero_scene_1() -> Tuple[str, str]:
    """#1 EU 22nd Russia sanctions: EU stars, bank & shadow tanker under ban, 60 BANKS · 70 TANKERS."""
    stars = []
    for i in range(12):
        ang = math.radians(i * 30)
        sx = 46 + 22 * math.cos(ang)
        sy = 38 + 22 * math.sin(ang)
        stars.append(f'<polygon points="{_star_points(sx, sy, 3.8, 1.6)}" fill="#FACC15"/>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#162C6E"/>
  <rect x="0" y="54" width="310" height="22" fill="#0F1F4D"/>
  <circle cx="46" cy="38" r="29" fill="#1E3A8A" stroke="#3B82F6" stroke-width="1"/>
  {''.join(stars)}
  <text x="46" y="38.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="13" fill="#FFFFFF">EU 22</text>
  <!-- Stylized bank icon -->
  <g transform="translate(88, 12)">
    <polygon points="18,0 36,9 0,9" fill="#CBD5E1"/>
    <rect x="3" y="10" width="5" height="14" fill="#E2E8F0"/>
    <rect x="11.5" y="10" width="5" height="14" fill="#E2E8F0"/>
    <rect x="20" y="10" width="5" height="14" fill="#E2E8F0"/>
    <rect x="28" y="10" width="5" height="14" fill="#E2E8F0"/>
    <rect x="0" y="25" width="36" height="3.5" fill="#94A3B8"/>
  </g>
  <!-- Stylized shadow-fleet tanker -->
  <g transform="translate(142, 16)">
    <polygon points="0,14 68,14 60,24 6,24" fill="#64748B"/>
    <rect x="10" y="8" width="16" height="6" fill="#94A3B8"/>
    <rect x="30" y="8" width="16" height="6" fill="#94A3B8"/>
    <rect x="50" y="3" width="10" height="11" fill="#CBD5E1"/>
    <rect x="53" y="0" width="4" height="3" fill="#EF4444"/>
  </g>
  <!-- Red sanction rings -->
  <circle cx="106" cy="26" r="14" fill="none" stroke="#EF4444" stroke-width="2.6"/>
  <line x1="96" y1="16" x2="116" y2="36" stroke="#EF4444" stroke-width="2.6"/>
  <circle cx="176" cy="28" r="14" fill="none" stroke="#EF4444" stroke-width="2.6"/>
  <line x1="166" y1="18" x2="186" y2="38" stroke="#EF4444" stroke-width="2.6"/>
  <!-- Crypto hexagon barred -->
  <g transform="translate(226, 12)">
    <polygon points="16,0 30,8 30,22 16,30 2,22 2,8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.8"/>
    <text x="16" y="15.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="12" fill="#FBBF24">₿</text>
    <line x1="4" y1="4" x2="28" y2="26" stroke="#EF4444" stroke-width="2.4"/>
  </g>
  {_banner(88, 46, 212, 24, "60 BANKS · 70 TANKERS", "#B91C1C", "#FCA5A5", 1.2, 12.5)}
</svg>"""
    return "#162C6E", svg


def hero_scene_2() -> Tuple[str, str]:
    """#2 US blacklists Iran shadow-bank network: Treasury + Tehran nodes + 24+ FRONTS HIT / IRAN OFAC SANCTIONS."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#1C1917"/>
  <rect x="0" y="0" width="310" height="3" fill="#D97706"/>
  <!-- US Treasury pediment left -->
  <g transform="translate(8, 8)">
    <polygon points="27,0 54,11 0,11" fill="#FACC15"/>
    <rect x="4" y="12" width="6" height="24" fill="#FFFFFF"/>
    <rect x="15.5" y="12" width="6" height="24" fill="#FFFFFF"/>
    <rect x="27" y="12" width="6" height="24" fill="#FFFFFF"/>
    <rect x="38.5" y="12" width="6" height="24" fill="#FFFFFF"/>
    <rect x="47.5" y="12" width="3.5" height="24" fill="#E2E8F0"/>
    <rect x="0" y="37" width="54" height="5" fill="#D97706"/>
    <text x="27" y="55" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="9.2" fill="#FDE68A">US TREASURY</text>
  </g>
  <!-- Shadow network links cut -->
  <line x1="68" y1="24" x2="108" y2="24" stroke="#F59E0B" stroke-width="2.2" stroke-dasharray="4,3"/>
  <line x1="68" y1="40" x2="108" y2="40" stroke="#F59E0B" stroke-width="2.2" stroke-dasharray="4,3"/>
  <circle cx="88" cy="32" r="10.5" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.6"/>
  <line x1="83" y1="27" x2="93" y2="37" stroke="#FFFFFF" stroke-width="2.4"/>
  <line x1="93" y1="27" x2="83" y2="37" stroke="#FFFFFF" stroke-width="2.4"/>
  <!-- Tehran arch / front hub -->
  <g transform="translate(110, 9)">
    <path d="M4,41 L10,13 L18,3 L26,13 L32,41 L24,41 L22,26 Q18,21 14,26 L12,41 Z" fill="#F5F5F4"/>
    <circle cx="18" cy="12" r="3.2" fill="#F59E0B"/>
    <text x="18" y="54" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="9.2" fill="#F5F5F4">TEHRAN</text>
  </g>
  {_banner(152, 8, 152, 27, "24+ FRONTS HIT", "#B91C1C", "#FECACA", 1.4, 12.6)}
  {_banner(152, 41, 152, 27, "IRAN OFAC SANCTIONS", "#1E3A8A", "#FACC15", 1.5, 10.8, "#FFFFFF")}
</svg>"""
    return "#1C1917", svg


def hero_scene_3() -> Tuple[str, str]:
    """#3 Drones strike Russia's Perm Lukoil refinery: refinery silhouette, blast, drone arc, 1,500 KM STRIKE."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#1E293B"/>
  <rect x="0" y="58" width="310" height="18" fill="#0F172A"/>
  <!-- Flight arc & drone -->
  <path d="M12,24 Q70,4 128,31" fill="none" stroke="#F87171" stroke-width="1.8" stroke-dasharray="4,3"/>
  <polygon points="34,15 52,19 36,24 40,19" fill="#E2E8F0"/>
  <!-- Refinery towers & storage tanks -->
  <rect x="86" y="34" width="10" height="26" fill="#475569"/>
  <rect x="100" y="20" width="12" height="40" fill="#64748B"/>
  <rect x="116" y="28" width="10" height="32" fill="#475569"/>
  <rect x="64" y="42" width="18" height="18" rx="2" fill="#334155"/>
  <rect x="132" y="39" width="22" height="21" rx="2" fill="#475569"/>
  <!-- Smoke & blast -->
  <circle cx="128" cy="18" r="10" fill="#64748B" opacity="0.65"/>
  <circle cx="140" cy="12" r="12" fill="#475569" opacity="0.55"/>
  <polygon points="124,22 130,30 140,26 134,36 144,42 132,43 130,53 123,44 112,46 119,37 112,29 122,31" fill="#F97316"/>
  <polygon points="125,28 129,34 136,33 131,39 135,44 128,42 125,47 122,41 116,42 121,37 118,32 124,33" fill="#FDE047"/>
  {_banner(160, 12, 140, 26, "1,500 KM STRIKE", "#B91C1C", "#FCA5A5", 1.2, 12.2)}
  {_banner(160, 44, 140, 24, "PERM · 3 UNITS HIT", "#0F172A", "#64748B", 1.1, 10.5, "#E2E8F0")}
</svg>"""
    return "#1E293B", svg


def mid_scene_4() -> Tuple[str, str]:
    """#4 Copernicus satellite deal: dark #090F24 space, satellite scan cone, €240m+."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#090F24"/>
  <!-- Stars -->
  <circle cx="16" cy="12" r="1.3" fill="#E2E8F0"/>
  <circle cx="48" cy="9" r="1.1" fill="#93C5FD"/>
  <circle cx="96" cy="14" r="1.4" fill="#FFFFFF"/>
  <circle cx="118" cy="8" r="1.1" fill="#BAE6FD"/>
  <!-- Earth limb -->
  <path d="M0,62 Q68,44 148,68 L0,70 Z" fill="#0369A1"/>
  <path d="M0,62 Q68,44 148,68" fill="none" stroke="#38BDF8" stroke-width="2"/>
  <!-- Radar scan beam -->
  <polygon points="56,28 34,58 78,56" fill="#38BDF8" opacity="0.28"/>
  <!-- Satellite -->
  <rect x="48" y="18" width="16" height="11" rx="1.5" fill="#F59E0B" stroke="#FEF3C7" stroke-width="1"/>
  <rect x="22" y="20" width="23" height="7" fill="#2563EB" stroke="#93C5FD" stroke-width="0.9"/>
  <rect x="67" y="20" width="23" height="7" fill="#2563EB" stroke="#93C5FD" stroke-width="0.9"/>
  {_banner(100, 18, 108, 34, "€240m+", "#0F172A", "#38BDF8", 1.5, 16.0)}
</svg>"""
    return "#090F24", svg


def mid_scene_5() -> Tuple[str, str]:
    """#5 Gaza UNRWA water well: Mediterranean coast, blue UN water drop + burst, GAZA AID HIT."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#0369A1"/>
  <!-- Mediterranean wave highlights -->
  <path d="M3,20 Q12,16 21,20 M2,44 Q11,40 20,44" fill="none" stroke="#7DD3FC" stroke-width="1.3" opacity="0.75"/>
  <!-- Mediterranean coast & land -->
  <path d="M36,0 L216,0 L216,70 L18,70 Q34,38 36,0 Z" fill="#E7D8C0"/>
  <path d="M36,0 Q34,38 18,70" fill="none" stroke="#0284C7" stroke-width="2.8"/>
  <!-- Blue UN water drop -->
  <path d="M53,12 C53,12 37,33 37,45 A16,16 0 0,0 69,45 C69,33 53,12 53,12 Z" fill="#0284C7" stroke="#FFFFFF" stroke-width="2.0"/>
  <circle cx="48" cy="44" r="3.4" fill="#E0F2FE"/>
  <!-- Impact burst -->
  <polygon points="70,13 74,21 82,19 77,26 83,32 75,32 72,39 68,32 61,33 65,26 62,19 68,21" fill="#B91C1C"/>
  <circle cx="71" cy="26" r="3.8" fill="#FDE047"/>
  {_banner(84, 17, 126, 36, "GAZA AID HIT", "#991B1B", "#FFFFFF", 1.8, 14.2)}
</svg>"""
    return "linear-gradient(90deg, #0369A1 0%, #0369A1 50%, #E7D8C0 50%, #E7D8C0 100%)", svg


def mid_scene_6() -> Tuple[str, str]:
    """#6 Villavicencio car bomb: urban skyline + blast starburst, 23 HURT."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#1E293B"/>
  <rect x="0" y="56" width="216" height="14" fill="#0F172A"/>
  <!-- Urban blocks -->
  <rect x="8" y="22" width="18" height="36" fill="#334155"/>
  <rect x="30" y="14" width="20" height="44" fill="#475569"/>
  <rect x="54" y="28" width="16" height="30" fill="#334155"/>
  <rect x="74" y="20" width="18" height="38" fill="#475569"/>
  <!-- Blast starburst -->
  <polygon points="54,14 60,27 74,22 66,35 80,42 64,44 62,57 52,46 39,51 45,38 33,31 47,29" fill="#EF4444"/>
  <polygon points="54,22 58,31 67,29 61,37 68,42 58,42 56,49 50,42 43,44 47,37 41,32 50,32" fill="#FACC15"/>
  {_banner(94, 18, 114, 34, "23 HURT", "#B91C1C", "#FCA5A5", 1.5, 16.0)}
</svg>"""
    return "#1E293B", svg


def mid_scene_7() -> Tuple[str, str]:
    """#7 Vanuatu M6.5 quake: deep ocean seismograph wave + M 6.5 DEEP."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#0C4A6E"/>
  <line x1="0" y1="35" x2="216" y2="35" stroke="#0369A1" stroke-width="1.2"/>
  <circle cx="50" cy="35" r="24" fill="none" stroke="#38BDF8" stroke-width="1.2" opacity="0.45"/>
  <circle cx="50" cy="35" r="14" fill="none" stroke="#38BDF8" stroke-width="1.4" opacity="0.7"/>
  <!-- Seismograph spike -->
  <polyline points="4,35 18,35 24,31 30,40 36,24 42,50 49,10 56,59 63,17 70,46 76,29 82,37 88,35" fill="none" stroke="#F8FAFC" stroke-width="2.4" stroke-linejoin="round"/>
  {_banner(90, 18, 118, 34, "M 6.5 DEEP", "#0F172A", "#38BDF8", 1.5, 14.8)}
</svg>"""
    return "#0C4A6E", svg


def mid_scene_8() -> Tuple[str, str]:
    """#8 NZ vs India cricket draw: green pitch, stumps & ball, DAY 5 DRAW."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#166534"/>
  <polygon points="8,70 26,22 70,22 86,70" fill="#D6C49C"/>
  <!-- Stumps & bails -->
  <rect x="36" y="14" width="4.5" height="44" rx="1" fill="#F8FAFC"/>
  <rect x="46" y="14" width="4.5" height="44" rx="1" fill="#F8FAFC"/>
  <rect x="56" y="14" width="4.5" height="44" rx="1" fill="#F8FAFC"/>
  <rect x="35" y="11" width="13" height="3.2" rx="1" fill="#FDE047"/>
  <rect x="49" y="11" width="13" height="3.2" rx="1" fill="#FDE047"/>
  <!-- Red cricket ball -->
  <circle cx="74" cy="48" r="7.5" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.2"/>
  <path d="M69,44 Q74,48 79,52" fill="none" stroke="#FEF2F2" stroke-width="1.1"/>
  {_banner(88, 18, 120, 34, "DAY 5 DRAW", "#0F172A", "#86EFAC", 1.5, 14.2)}
</svg>"""
    return "#166534", svg


def mid_scene_9() -> Tuple[str, str]:
    """#9 IMF Ecuador loan: rising bar chart + upward arrow, $377m IMF."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#3B0764"/>
  <line x1="10" y1="58" x2="84" y2="58" stroke="#C084FC" stroke-width="1.5"/>
  <rect x="14" y="42" width="12" height="16" rx="1.5" fill="#A855F7"/>
  <rect x="31" y="33" width="12" height="25" rx="1.5" fill="#C084FC"/>
  <rect x="48" y="23" width="12" height="35" rx="1.5" fill="#34D399"/>
  <rect x="65" y="13" width="12" height="45" rx="1.5" fill="#FACC15"/>
  <polyline points="14,35 36,24 56,15 74,8" fill="none" stroke="#FFFFFF" stroke-width="2"/>
  <polygon points="76,7 68,7 73,14" fill="#FFFFFF"/>
  {_banner(88, 18, 120, 34, "$377m IMF", "#0F172A", "#FACC15", 1.5, 14.8)}
</svg>"""
    return "#3B0764", svg


def mid_scene_10() -> Tuple[str, str]:
    """#10 Kenya & DRC restore ambassadors: diplomatic nodes + bidirectional arrows, ENVOYS BACK."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#1F2937"/>
  <!-- Left & right embassy badges -->
  <circle cx="22" cy="35" r="13.5" fill="#991B1B" stroke="#F8FAFC" stroke-width="1.6"/>
  <text x="22" y="35.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="10" fill="#FFFFFF">KE</text>
  <circle cx="72" cy="35" r="13.5" fill="#1D4ED8" stroke="#F8FAFC" stroke-width="1.6"/>
  <text x="72" y="35.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="9.5" fill="#FDE047">DRC</text>
  <!-- Bidirectional arrows -->
  <line x1="38" y1="29" x2="54" y2="29" stroke="#34D399" stroke-width="2.4"/>
  <polygon points="57,29 51,25 51,33" fill="#34D399"/>
  <line x1="39" y1="41" x2="55" y2="41" stroke="#FACC15" stroke-width="2.4"/>
  <polygon points="36,41 42,37 42,45" fill="#FACC15"/>
  {_banner(90, 18, 120, 34, "ENVOYS BACK", "#047857", "#A7F3D0", 1.4, 13.6)}
</svg>"""
    return "#1F2937", svg


def mid_scene_11() -> Tuple[str, str]:
    """#11 South Korea scrambles jets: tactical green radar + aircraft blips, 22:52 UTC."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#052E16"/>
  <circle cx="46" cy="35" r="28" fill="#064E3B" stroke="#22C55E" stroke-width="1.4"/>
  <circle cx="46" cy="35" r="19" fill="none" stroke="#22C55E" stroke-width="1" opacity="0.7"/>
  <circle cx="46" cy="35" r="10" fill="none" stroke="#22C55E" stroke-width="1" opacity="0.7"/>
  <line x1="18" y1="35" x2="74" y2="35" stroke="#22C55E" stroke-width="0.9" opacity="0.6"/>
  <line x1="46" y1="7" x2="46" y2="63" stroke="#22C55E" stroke-width="0.9" opacity="0.6"/>
  <path d="M46,35 L68,18 A28,28 0 0,1 73,35 Z" fill="#4ADE80" opacity="0.32"/>
  <!-- Fighter & bogey blips -->
  <polygon points="35,43 44,38 39,47" fill="#FFFFFF"/>
  <circle cx="60" cy="23" r="3.4" fill="#EF4444" stroke="#FEF2F2" stroke-width="1"/>
  {_banner(86, 18, 122, 34, "22:52 UTC", "#0F172A", "#4ADE80", 1.5, 15.2)}
</svg>"""
    return "#052E16", svg


def mid_scene_12() -> Tuple[str, str]:
    """#12 Abu Dhabi crypto freeze: padlock + chain + ice-blue freeze, 18 FIRMS."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#1C1917"/>
  <!-- Ice-blue crypto freeze halo behind lock -->
  <polygon points="45,5 68,18 68,46 45,60 22,46 22,18" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.2" opacity="0.55"/>
  <!-- Chain links -->
  <rect x="5" y="31" width="19" height="10" rx="5" fill="none" stroke="#CBD5E1" stroke-width="2.6"/>
  <rect x="66" y="31" width="19" height="10" rx="5" fill="none" stroke="#CBD5E1" stroke-width="2.6"/>
  <!-- Padlock -->
  <path d="M33,31 L33,20 A12,12 0 0,1 57,20 L57,31" fill="none" stroke="#7DD3FC" stroke-width="4.2"/>
  <rect x="26" y="29" width="38" height="29" rx="4" fill="#F59E0B" stroke="#FEF08A" stroke-width="1.8"/>
  <circle cx="45" cy="41.5" r="4.2" fill="#1C1917"/>
  <rect x="43" y="44" width="4" height="7.5" fill="#1C1917"/>
  {_banner(90, 17, 118, 36, "18 FIRMS", "#0F172A", "#FACC15", 1.8, 15.8)}
</svg>"""
    return "#1C1917", svg


def mid_scene_13() -> Tuple[str, str]:
    """#13 CAF AFCON 2027 sponsor: gold trophy cup + star, AFCON 2027."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#450A0A"/>
  <!-- Trophy handles -->
  <path d="M30,18 C20,18 20,34 32,34" fill="none" stroke="#FACC15" stroke-width="2.8"/>
  <path d="M56,18 C66,18 66,34 54,34" fill="none" stroke="#FACC15" stroke-width="2.8"/>
  <!-- Trophy cup -->
  <path d="M30,14 L56,14 L52,36 Q43,44 34,36 Z" fill="#FACC15" stroke="#FEF08A" stroke-width="1.2"/>
  <rect x="40" y="40" width="6" height="10" fill="#EAB308"/>
  <rect x="31" y="50" width="24" height="6" rx="1.5" fill="#FDE047"/>
  <polygon points="{_star_points(43, 25, 6.2, 2.7)}" fill="#991B1B"/>
  {_banner(82, 18, 126, 34, "AFCON 2027", "#991B1B", "#FACC15", 1.5, 14.8)}
</svg>"""
    return "#450A0A", svg


SCENE_BUILDERS = {
    1: hero_scene_1,
    2: hero_scene_2,
    3: hero_scene_3,
    4: mid_scene_4,
    5: mid_scene_5,
    6: mid_scene_6,
    7: mid_scene_7,
    8: mid_scene_8,
    9: mid_scene_9,
    10: mid_scene_10,
    11: mid_scene_11,
    12: mid_scene_12,
    13: mid_scene_13,
}


def get_scene(num: int) -> Tuple[str, str]:
    return SCENE_BUILDERS[num]()


def build_world_map_svg() -> str:
    """Clean SVG world map (viewBox 0 0 360 172) with 13 numbered region pins."""
    pins_svg: List[str] = []
    for num, reg_id, x, y in MAP_PINS:
        color = str(REGION_BY_ID[reg_id]["color"])
        font_sz = 10.8 if num < 10 else 9.8
        pins_svg.append(
            f'<g class="map-pin" data-num="{num}" data-x="{x:.1f}" data-y="{y:.1f}">'
            f'<circle cx="{x:.1f}" cy="{y + 0.6:.1f}" r="12.3" fill="#0F172A" opacity="0.22"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11.4" fill="{color}" stroke="#FFFFFF" stroke-width="1.9"/>'
            f'<text x="{x:.1f}" y="{y + 0.4:.1f}" text-anchor="middle" dominant-baseline="central" '
            f'font-family="{FONT_SANS}" font-weight="900" font-size="{font_sz:.1f}" fill="#FFFFFF">{num}</text>'
            f"</g>"
        )

    return f"""<svg id="world-map" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 172" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <rect width="360" height="172" fill="#D8EBF8"/>
  <!-- Subtle latitude/longitude grid -->
  <line x1="0" y1="86" x2="360" y2="86" stroke="#BBD7EA" stroke-width="0.7" stroke-dasharray="3,3"/>
  <line x1="180" y1="0" x2="180" y2="172" stroke="#BBD7EA" stroke-width="0.7" stroke-dasharray="3,3"/>
  <!-- Continents (#C7C0B0 with #78716C stroke) -->
  <g fill="#C7C0B0" stroke="#78716C" stroke-width="0.85" stroke-linejoin="round">
    <!-- North America -->
    <path d="M18,22 L54,14 L92,16 L112,28 L104,45 L95,55 L86,69 L75,78 L66,76 L58,64 L44,54 L36,40 L20,34 Z"/>
    <!-- Greenland -->
    <path d="M114,8 L142,8 L138,24 L120,25 Z"/>
    <!-- South America -->
    <path d="M84,84 L106,82 L126,96 L132,112 L121,134 L108,154 L96,158 L91,138 L83,115 L78,96 Z"/>
    <!-- Europe -->
    <path d="M164,20 L194,14 L218,18 L224,34 L210,44 L196,49 L180,49 L168,46 L160,36 Z"/>
    <!-- UK & Ireland -->
    <path d="M162,30 L167,29 L168,37 L162,38 Z"/>
    <!-- Africa -->
    <path d="M164,58 L196,55 L218,64 L228,84 L232,102 L222,126 L206,148 L192,144 L184,120 L176,98 L160,84 L158,68 Z"/>
    <!-- Madagascar -->
    <path d="M233,124 L238,123 L236,138 L231,137 Z"/>
    <!-- Asia & Middle East -->
    <path d="M214,18 L272,14 L322,22 L338,34 L326,48 L314,62 L298,74 L286,84 L274,78 L266,86 L256,74 L244,86 L232,82 L224,68 L212,56 L218,42 Z"/>
    <!-- Japan -->
    <path d="M324,46 L331,42 L334,54 L326,58 Z"/>
    <!-- Indonesia & Maritime SE Asia -->
    <path d="M286,96 L304,95 L306,102 L288,103 Z"/>
    <path d="M310,98 L322,97 L324,104 L311,104 Z"/>
    <!-- Australia -->
    <path d="M288,116 L318,114 L330,126 L326,144 L306,148 L290,140 L284,128 Z"/>
    <!-- New Zealand -->
    <path d="M342,143 L349,141 L347,156 L339,156 Z"/>
  </g>
  <!-- 13 Numbered Scene Pins -->
  {''.join(pins_svg)}
</svg>"""
