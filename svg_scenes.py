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
    """#1 EU 22nd Russia sanctions: EU stars + blocked bank/tanker/crypto + 60 BANKS · 70 TANKERS on #EFF6FF."""
    stars = []
    for i in range(12):
        ang = math.radians(i * 30)
        sx = 44 + 21 * math.cos(ang)
        sy = 38 + 21 * math.sin(ang)
        stars.append(f'<polygon points="{_star_points(sx, sy, 3.6, 1.5)}" fill="#FACC15"/>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#EFF6FF"/>
  <rect x="0" y="56" width="310" height="20" fill="#DBEAFE"/>
  <line x1="0" y1="56" x2="310" y2="56" stroke="#93C5FD" stroke-width="1"/>
  <!-- EU star circle left -->
  <circle cx="44" cy="38" r="28" fill="#1E3A8A" stroke="#1D4ED8" stroke-width="1.2"/>
  {''.join(stars)}
  <text x="44" y="38.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="12.5" fill="#FFFFFF">EU 22</text>
  <!-- Bank icon -->
  <g transform="translate(88, 10)">
    <polygon points="18,0 36,9 0,9" fill="#1E3A8A"/>
    <rect x="3" y="10" width="5" height="14" fill="#334155"/>
    <rect x="11.5" y="10" width="5" height="14" fill="#334155"/>
    <rect x="20" y="10" width="5" height="14" fill="#334155"/>
    <rect x="28" y="10" width="5" height="14" fill="#334155"/>
    <rect x="0" y="25" width="36" height="3.5" fill="#1E3A8A"/>
  </g>
  <!-- Shadow-fleet tanker -->
  <g transform="translate(143, 14)">
    <polygon points="0,14 68,14 60,24 6,24" fill="#334155"/>
    <rect x="10" y="8" width="16" height="6" fill="#64748B"/>
    <rect x="30" y="8" width="16" height="6" fill="#64748B"/>
    <rect x="50" y="3" width="10" height="11" fill="#475569"/>
    <rect x="53" y="0" width="4" height="3" fill="#DC2626"/>
  </g>
  <!-- Red sanction rings -->
  <circle cx="106" cy="24" r="14" fill="none" stroke="#DC2626" stroke-width="2.6"/>
  <line x1="96" y1="14" x2="116" y2="34" stroke="#DC2626" stroke-width="2.6"/>
  <circle cx="177" cy="26" r="14" fill="none" stroke="#DC2626" stroke-width="2.6"/>
  <line x1="167" y1="16" x2="187" y2="36" stroke="#DC2626" stroke-width="2.6"/>
  <!-- Crypto hexagon barred -->
  <g transform="translate(229, 10)">
    <polygon points="16,0 30,8 30,22 16,30 2,22 2,8" fill="#1E293B" stroke="#D97706" stroke-width="1.8"/>
    <text x="16" y="15.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="12" fill="#FACC15">₿</text>
    <line x1="4" y1="4" x2="28" y2="26" stroke="#DC2626" stroke-width="2.5"/>
  </g>
  {_banner(86, 45, 214, 25, "60 BANKS · 70 TANKERS", "#B91C1C", "#FFFFFF", 1.4, 12.6)}
</svg>"""
    return "#EFF6FF", svg


def hero_scene_2() -> Tuple[str, str]:
    """#2 US blacklists Iran shadow-bank network: Treasury columns + blocked arc + Tehran arch on #FFFBEB."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#FFFBEB"/>
  <rect x="0" y="59" width="310" height="17" fill="#FEF3C7"/>
  <line x1="0" y1="59" x2="310" y2="59" stroke="#F59E0B" stroke-width="1"/>
  <!-- US Treasury pediment left -->
  <g transform="translate(8, 8)">
    <polygon points="27,0 54,11 0,11" fill="#B45309"/>
    <rect x="4" y="12" width="6" height="24" fill="#1E293B"/>
    <rect x="15.5" y="12" width="6" height="24" fill="#1E293B"/>
    <rect x="27" y="12" width="6" height="24" fill="#1E293B"/>
    <rect x="38.5" y="12" width="6" height="24" fill="#1E293B"/>
    <rect x="47.5" y="12" width="3.5" height="24" fill="#475569"/>
    <rect x="0" y="37" width="54" height="5" fill="#B45309"/>
    <text x="27" y="55" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="9.0" fill="#78350F">US TREASURY</text>
  </g>
  <!-- Blocked illicit-flow arc -->
  <path d="M67,38 Q88,16 109,38" fill="none" stroke="#D97706" stroke-width="2.2" stroke-dasharray="4,3"/>
  <line x1="67" y1="38" x2="109" y2="38" stroke="#D97706" stroke-width="1.8" stroke-dasharray="4,3"/>
  <circle cx="88" cy="31" r="10.5" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.6"/>
  <line x1="83" y1="26" x2="93" y2="36" stroke="#FFFFFF" stroke-width="2.4"/>
  <line x1="93" y1="26" x2="83" y2="36" stroke="#FFFFFF" stroke-width="2.4"/>
  <!-- Tehran arch -->
  <g transform="translate(111, 9)">
    <path d="M4,41 L10,13 L18,3 L26,13 L32,41 L24,41 L22,26 Q18,21 14,26 L12,41 Z" fill="#334155"/>
    <circle cx="18" cy="12" r="3.2" fill="#F59E0B"/>
    <text x="18" y="54" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="9.0" fill="#1E293B">TEHRAN</text>
  </g>
  {_banner(152, 8, 152, 27, "24+ FRONTS HIT", "#B91C1C", "#FFFFFF", 1.4, 12.6)}
  {_banner(152, 41, 152, 27, "IRAN OFAC SANCTIONS", "#1E3A8A", "#D97706", 1.5, 10.8, "#FFFFFF")}
</svg>"""
    return "#FFFBEB", svg


def hero_scene_3() -> Tuple[str, str]:
    """#3 Drones strike Russia's Perm Lukoil refinery: wide refinery strike on #F1F5F9."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#F1F5F9"/>
  <rect x="0" y="59" width="310" height="17" fill="#CBD5E1"/>
  <line x1="0" y1="59" x2="310" y2="59" stroke="#94A3B8" stroke-width="1.2"/>
  <!-- Long-range drone flight arc -->
  <path d="M10,22 Q68,4 124,29" fill="none" stroke="#DC2626" stroke-width="2.0" stroke-dasharray="4,3"/>
  <polygon points="32,12 52,17 34,23 39,17" fill="#0F172A"/>
  <!-- Refinery towers & storage tanks -->
  <rect x="60" y="42" width="18" height="17" rx="2" fill="#64748B" stroke="#334155" stroke-width="0.9"/>
  <rect x="83" y="32" width="11" height="27" fill="#475569"/>
  <rect x="98" y="18" width="13" height="41" fill="#334155"/>
  <rect x="115" y="27" width="11" height="32" fill="#475569"/>
  <rect x="131" y="40" width="22" height="19" rx="2" fill="#64748B" stroke="#334155" stroke-width="0.9"/>
  <!-- Smoke plume & impact burst -->
  <circle cx="127" cy="17" r="9.5" fill="#94A3B8" opacity="0.8"/>
  <circle cx="140" cy="11" r="11" fill="#64748B" opacity="0.6"/>
  <polygon points="122,20 128,29 138,25 132,35 142,41 130,42 128,53 121,43 110,45 117,36 110,28 120,30" fill="#DC2626"/>
  <polygon points="123,27 127,33 134,32 129,38 133,43 126,41 123,46 120,40 114,41 119,36 116,31 122,32" fill="#FACC15"/>
  {_banner(158, 9, 144, 27, "1,500 KM STRIKE", "#B91C1C", "#FFFFFF", 1.4, 12.6)}
  {_banner(158, 41, 144, 26, "PERM · 3 UNITS HIT", "#0F172A", "#64748B", 1.2, 10.8, "#F8FAFC")}
</svg>"""
    return "#F1F5F9", svg


def mid_scene_4() -> Tuple[str, str]:
    """#4 Copernicus satellite deal: dark #090F24 orbital satellite scene with €240m+ pill."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#090F24"/>
  <!-- Stars -->
  <circle cx="16" cy="12" r="1.3" fill="#E2E8F0"/>
  <circle cx="48" cy="9" r="1.1" fill="#93C5FD"/>
  <circle cx="94" cy="14" r="1.4" fill="#FFFFFF"/>
  <!-- Earth limb (ocean & ice) -->
  <path d="M0,61 Q66,43 144,68 L0,70 Z" fill="#0369A1"/>
  <path d="M12,63 Q46,53 84,59 Q64,66 28,67 Z" fill="#E0F2FE" opacity="0.82"/>
  <path d="M0,61 Q66,43 144,68" fill="none" stroke="#38BDF8" stroke-width="2"/>
  <!-- Altimeter scan cone -->
  <polygon points="56,28 33,58 79,56" fill="#38BDF8" opacity="0.28"/>
  <!-- Satellite -->
  <rect x="48" y="17" width="16" height="11" rx="1.5" fill="#F59E0B" stroke="#FEF3C7" stroke-width="1"/>
  <rect x="20" y="19" width="25" height="7" fill="#2563EB" stroke="#93C5FD" stroke-width="0.9"/>
  <rect x="67" y="19" width="25" height="7" fill="#2563EB" stroke="#93C5FD" stroke-width="0.9"/>
  {_banner(100, 18, 108, 34, "€240m+", "#0F172A", "#38BDF8", 1.5, 16.0)}
</svg>"""
    return "#090F24", svg


def mid_scene_5() -> Tuple[str, str]:
    """#5 Gaza UNRWA water well: Mediterranean coast + blue water drop + burst + GAZA AID HIT on #F1F5F9."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#F1F5F9"/>
  <!-- Mediterranean bay left -->
  <path d="M0,0 L35,0 Q32,38 17,70 L0,70 Z" fill="#0369A1"/>
  <path d="M3,20 Q12,16 21,20 M2,44 Q11,40 20,44" fill="none" stroke="#7DD3FC" stroke-width="1.3" opacity="0.8"/>
  <!-- Coastal strip -->
  <path d="M35,0 L88,0 L88,70 L17,70 Q32,38 35,0 Z" fill="#E7D8C0"/>
  <path d="M35,0 Q32,38 17,70" fill="none" stroke="#0284C7" stroke-width="2.6"/>
  <!-- Blue UN water drop -->
  <path d="M53,12 C53,12 37,33 37,45 A16,16 0 0,0 69,45 C69,33 53,12 53,12 Z" fill="#0284C7" stroke="#FFFFFF" stroke-width="2.0"/>
  <circle cx="48" cy="44" r="3.4" fill="#E0F2FE"/>
  <!-- Impact burst -->
  <polygon points="70,13 74,21 82,19 77,26 83,32 75,32 72,39 68,32 61,33 65,26 62,19 68,21" fill="#B91C1C"/>
  <circle cx="71" cy="26" r="3.8" fill="#FDE047"/>
  {_banner(84, 17, 126, 36, "GAZA AID HIT", "#991B1B", "#FFFFFF", 1.6, 14.2)}
</svg>"""
    return "#F1F5F9", svg


def mid_scene_6() -> Tuple[str, str]:
    """#6 Villavicencio car bomb: urban blast scene + 23 HURT pill on #FEF3C7."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#FEF3C7"/>
  <rect x="0" y="56" width="216" height="14" fill="#FDE68A"/>
  <line x1="0" y1="56" x2="216" y2="56" stroke="#D97706" stroke-width="1.1"/>
  <!-- Urban blocks -->
  <rect x="8" y="22" width="18" height="34" fill="#475569"/>
  <rect x="30" y="13" width="20" height="43" fill="#334155"/>
  <rect x="54" y="27" width="16" height="29" fill="#475569"/>
  <rect x="74" y="19" width="18" height="37" fill="#334155"/>
  <!-- Blast starburst -->
  <polygon points="54,13 60,26 74,21 66,34 80,41 64,43 62,56 52,45 39,50 45,37 33,30 47,28" fill="#DC2626"/>
  <polygon points="54,21 58,30 67,28 61,36 68,41 58,41 56,48 50,41 43,43 47,36 41,31 50,31" fill="#FACC15"/>
  {_banner(94, 17, 114, 36, "23 HURT", "#B91C1C", "#FFFFFF", 1.6, 16.0)}
</svg>"""
    return "#FEF3C7", svg


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
