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
    """#1 Drones strike Russia's Perm Lukoil refinery: wide refinery strike on #F1F5F9 sky."""
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


def hero_scene_2() -> Tuple[str, str]:
    """#2 Thales Copernicus satellite deal: dark #090F24 orbital Earth-limb scene with €240m+ & SENTINEL 3NG CLIMATE."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#090F24"/>
  <!-- Stars -->
  <circle cx="14" cy="12" r="1.2" fill="#E2E8F0"/>
  <circle cx="42" cy="8" r="1.0" fill="#93C5FD"/>
  <circle cx="114" cy="11" r="1.4" fill="#FFFFFF"/>
  <circle cx="138" cy="18" r="1.1" fill="#BAE6FD"/>
  <!-- Glowing ocean & ice Earth limb -->
  <path d="M0,62 Q78,41 168,72 L0,76 Z" fill="#0369A1"/>
  <path d="M18,64 Q56,52 98,58 Q74,66 36,68 Z" fill="#E0F2FE" opacity="0.85"/>
  <path d="M0,62 Q78,41 168,72" fill="none" stroke="#38BDF8" stroke-width="2.2"/>
  <!-- Glowing cyan ocean/ice altimeter scan beam -->
  <polygon points="68,30 34,62 104,60" fill="#38BDF8" opacity="0.28"/>
  <line x1="68" y1="30" x2="68" y2="57" stroke="#7DD3FC" stroke-width="1.4" stroke-dasharray="3,2"/>
  <!-- Sentinel 3NG satellite array -->
  <rect x="57" y="17" width="22" height="13" rx="2" fill="#F59E0B" stroke="#FEF3C7" stroke-width="1.2"/>
  <rect x="20" y="19" width="33" height="9" rx="1" fill="#2563EB" stroke="#93C5FD" stroke-width="1.1"/>
  <line x1="31" y1="19" x2="31" y2="28" stroke="#93C5FD" stroke-width="0.8"/>
  <line x1="42" y1="19" x2="42" y2="28" stroke="#93C5FD" stroke-width="0.8"/>
  <rect x="83" y="19" width="33" height="9" rx="1" fill="#2563EB" stroke="#93C5FD" stroke-width="1.1"/>
  <line x1="94" y1="19" x2="94" y2="28" stroke="#93C5FD" stroke-width="0.8"/>
  <line x1="105" y1="19" x2="105" y2="28" stroke="#93C5FD" stroke-width="0.8"/>
  {_banner(144, 8, 158, 27, "€240m+", "#0284C7", "#E0F2FE", 1.5, 14.2)}
  {_banner(144, 41, 158, 27, "SENTINEL 3NG CLIMATE", "#0F172A", "#38BDF8", 1.4, 10.4, "#FFFFFF")}
</svg>"""
    return "#090F24", svg


def hero_scene_3() -> Tuple[str, str]:
    """#3 Villavicencio car bomb: wide urban blast on warm amber #FEF3C7 ground."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 310 76" width="100%" height="80" preserveAspectRatio="xMidYMid meet">
  <rect width="310" height="76" fill="#FEF3C7"/>
  <rect x="0" y="59" width="310" height="17" fill="#FDE68A"/>
  <line x1="0" y1="59" x2="310" y2="59" stroke="#D97706" stroke-width="1.2"/>
  <!-- Commercial urban blocks -->
  <rect x="10" y="24" width="22" height="35" fill="#475569"/>
  <rect x="36" y="13" width="26" height="46" fill="#334155"/>
  <rect x="66" y="29" width="20" height="30" fill="#475569"/>
  <rect x="90" y="19" width="26" height="40" fill="#334155"/>
  <rect x="120" y="31" width="20" height="28" fill="#64748B"/>
  <!-- Shockwave rings -->
  <circle cx="76" cy="39" r="26" fill="none" stroke="#DC2626" stroke-width="1.3" stroke-dasharray="3,2" opacity="0.65"/>
  <!-- Blast starburst -->
  <polygon points="76,12 83,27 99,21 90,36 105,44 87,46 84,61 73,49 58,54 65,40 51,32 68,30" fill="#DC2626"/>
  <polygon points="76,21 80,31 91,29 84,38 92,44 80,44 78,52 71,44 63,46 68,38 61,32 71,33" fill="#FACC15"/>
  {_banner(148, 8, 154, 27, "23 INJURED", "#B91C1C", "#FFFFFF", 1.5, 13.4)}
  {_banner(148, 41, 154, 27, "VILLAVICENCIO BLAST", "#0F172A", "#D97706", 1.4, 10.4, "#FFFFFF")}
</svg>"""
    return "#FEF3C7", svg


def mid_scene_4() -> Tuple[str, str]:
    """#4 EU 22nd Russia sanctions: EU stars + blocked tanker/crypto + 60 BANKS · 70 TANKERS on #EFF6FF."""
    stars = []
    for i in range(12):
        ang = math.radians(i * 30)
        sx = 34 + 13.5 * math.cos(ang)
        sy = 20 + 13.5 * math.sin(ang)
        stars.append(f'<polygon points="{_star_points(sx, sy, 2.7, 1.1)}" fill="#FACC15"/>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#EFF6FF"/>
  <!-- EU circle left -->
  <circle cx="34" cy="20" r="18" fill="#1E3A8A"/>
  {''.join(stars)}
  <text x="34" y="20.5" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="8.6" fill="#FFFFFF">EU 22</text>
  <!-- Blocked tanker center -->
  <g transform="translate(64, 10)">
    <polygon points="0,12 58,12 51,21 6,21" fill="#334155"/>
    <rect x="8" y="6" width="14" height="6" fill="#64748B"/>
    <rect x="25" y="6" width="14" height="6" fill="#64748B"/>
    <rect x="42" y="2" width="9" height="10" fill="#475569"/>
  </g>
  <circle cx="93" cy="21" r="13.5" fill="none" stroke="#DC2626" stroke-width="2.5"/>
  <line x1="83.5" y1="11.5" x2="102.5" y2="30.5" stroke="#DC2626" stroke-width="2.5"/>
  <!-- Blocked crypto badge right -->
  <g transform="translate(142, 6)">
    <polygon points="15,0 28,7.5 28,21.5 15,29 2,21.5 2,7.5" fill="#1E293B" stroke="#D97706" stroke-width="1.7"/>
    <text x="15" y="15" text-anchor="middle" dominant-baseline="central" font-family="{FONT_SANS}" font-weight="900" font-size="11.5" fill="#FACC15">₿</text>
    <line x1="4" y1="4" x2="26" y2="25" stroke="#DC2626" stroke-width="2.4"/>
  </g>
  <!-- Bank emblem far right -->
  <g transform="translate(179, 8)">
    <polygon points="13,0 26,7 0,7" fill="#1E3A8A"/>
    <rect x="3" y="8" width="4" height="12" fill="#334155"/>
    <rect x="11" y="8" width="4" height="12" fill="#334155"/>
    <rect x="19" y="8" width="4" height="12" fill="#334155"/>
    <rect x="0" y="21" width="26" height="3" fill="#1E3A8A"/>
  </g>
  {_banner(10, 41, 196, 25, "60 BANKS · 70 TANKERS", "#B91C1C", "#FFFFFF", 1.3, 11.4)}
</svg>"""
    return "#EFF6FF", svg


def mid_scene_5() -> Tuple[str, str]:
    """#5 US blacklists Iran shadow-bank network: Treasury + blocked flow + 24+ FRONTS HIT on #FFFBEB."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 216 70" width="100%" height="46" preserveAspectRatio="xMidYMid meet">
  <rect width="216" height="70" fill="#FFFBEB"/>
  <!-- US Treasury pediment left -->
  <g transform="translate(7, 13)">
    <polygon points="22,0 44,10 0,10" fill="#B45309"/>
    <rect x="3" y="11" width="5.5" height="22" fill="#1E293B"/>
    <rect x="13" y="11" width="5.5" height="22" fill="#1E293B"/>
    <rect x="23" y="11" width="5.5" height="22" fill="#1E293B"/>
    <rect x="33" y="11" width="5.5" height="22" fill="#1E293B"/>
    <rect x="0" y="34" width="44" height="4.5" fill="#B45309"/>
  </g>
  <!-- Blocked money flow -->
  <line x1="53" y1="27" x2="81" y2="27" stroke="#D97706" stroke-width="2.2" stroke-dasharray="4,3"/>
  <line x1="53" y1="41" x2="81" y2="41" stroke="#D97706" stroke-width="2.2" stroke-dasharray="4,3"/>
  <circle cx="67" cy="34" r="10.0" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.6"/>
  <line x1="62.5" y1="29.5" x2="71.5" y2="38.5" stroke="#FFFFFF" stroke-width="2.3"/>
  <line x1="71.5" y1="29.5" x2="62.5" y2="38.5" stroke="#FFFFFF" stroke-width="2.3"/>
  {_banner(83, 17, 128, 36, "24+ FRONTS HIT", "#B91C1C", "#FFFFFF", 1.5, 12.2)}
</svg>"""
    return "#FFFBEB", svg


def mid_scene_6() -> Tuple[str, str]:
    """#6 Gaza UNRWA water well: Mediterranean coast, blue UN water drop + strike burst, GAZA AID HIT on #F1F5F9."""
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
