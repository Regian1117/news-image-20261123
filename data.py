"""Structured dataset for the Monday 23 November 2026 world-news frontpage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

DATE_TITLE = "Monday 23 November 2026"
TOP_META_LEFT = "THE WORLD IN ONE DAY"
SUBHEAD = (
    "EU unveils 22nd Russia sanctions · US blacklists Iran shadow-bank network · "
    "Drones strike Perm Lukoil refinery"
)

REGIONS: List[Dict[str, object]] = [
    {"id": "europe", "name": "Europe", "upper": "EUROPE", "color": "#1E3A8A", "expected": 6},
    {"id": "middle_east", "name": "Middle East", "upper": "MIDDLE EAST", "color": "#D97706", "expected": 4},
    {"id": "africa", "name": "Africa", "upper": "AFRICA", "color": "#991B1B", "expected": 6},
    {"id": "east_asia", "name": "East Asia", "upper": "EAST ASIA", "color": "#15803D", "expected": 4},
    {"id": "south_se_asia", "name": "South & SE Asia", "upper": "SOUTH & SE ASIA", "color": "#0D9488", "expected": 2},
    {"id": "n_america", "name": "N. America", "upper": "N. AMERICA", "color": "#7C3AED", "expected": 3},
    {"id": "s_america", "name": "S. America", "upper": "S. AMERICA", "color": "#A21CAF", "expected": 3},
    {"id": "oceania", "name": "Oceania", "upper": "OCEANIA", "color": "#0284C7", "expected": 3},
    {"id": "world_space", "name": "World & Space", "upper": "WORLD & SPACE", "color": "#334155", "expected": 4},
]

REGION_BY_ID: Dict[str, Dict[str, object]] = {r["id"]: r for r in REGIONS}

TAG_COLORS: Dict[str, str] = {
    "CONFIRMED": "#047857",
    "OFFICIAL": "#0F766E",
    "REPORTED": "#1D4ED8",
    "CLAIM": "#B45309",
}

UTC_ANCHORS: List[str] = [
    "02:41 Vanuatu M6.5",
    "05:30 NZ–India draw",
    "07:30 Colombia bomb",
    "13:00 EU sanctions",
    "15:00 Iran OFAC",
    "16:00 Kilauea pause",
    "22:52 Korea jets",
]


@dataclass(frozen=True)
class FeatureStory:
    num: int
    region: str
    kicker: str
    tag: str
    headline_html: str
    deck: str
    source: str


@dataclass(frozen=True)
class BriefStory:
    num: int
    region: str
    subject: str
    text: str
    tag: str
    source: str
    inline_tag: bool = False


HERO_STORIES: List[FeatureStory] = [
    FeatureStory(
        num=1,
        region="europe",
        kicker="BRUSSELS · SANCTIONS",
        tag="OFFICIAL",
        headline_html="EU unveils 22nd Russia sanctions package",
        deck="Brussels proposes targeting 60 banks, 70 shadow-fleet tankers and crypto evasion networks.",
        source="Reuters · Al Jazeera",
    ),
    FeatureStory(
        num=2,
        region="middle_east",
        kicker="WASHINGTON · IRAN FINANCE",
        tag="OFFICIAL",
        headline_html='US blacklists <span class="sans-num">$14.7 billion</span> Iran shadow-bank network',
        deck="US Treasury sanctions 24+ currency exchanges and front firms across UAE, Turkey &amp; Hong Kong over illicit flows.",
        source="US Treasury · Reuters",
    ),
    FeatureStory(
        num=3,
        region="europe",
        kicker="PERM, RUSSIA · ENERGY WAR",
        tag="REPORTED",
        headline_html="Drones strike Russia's Perm Lukoil refinery",
        deck="Reports say long-range drones hit the refinery 1,500 km inside Russia, killing 1 and damaging 3 units.",
        source="AP · Reuters",
    ),
]

MID_STORIES: List[FeatureStory] = [
    FeatureStory(
        num=4,
        region="world_space",
        kicker="EUROPE · SPACE & CLIMATE",
        tag="OFFICIAL",
        headline_html='Thales signs <span class="sans-num">€240m+</span> Copernicus satellite deal',
        deck="Contract with Germany's OHB builds new Copernicus ocean and ice altimeters.",
        source="Reuters · Thales",
    ),
    FeatureStory(
        num=5,
        region="middle_east",
        kicker="GAZA · HUMANITARIAN",
        tag="REPORTED",
        headline_html="Strike near Jabalia water well kills UNRWA worker",
        deck="UN relief agency reports staffer killed near a northern Gaza water point; aid groups urge protection.",
        source="UNRWA · Reuters",
    ),
    FeatureStory(
        num=6,
        region="s_america",
        kicker="COLOMBIA · SECURITY",
        tag="REPORTED",
        headline_html="Car bomb injures 23 in Villavicencio blast",
        deck="Morning vehicle bombing damages commercial blocks; officials probe regional militants.",
        source="AP · Al Jazeera",
    ),
    FeatureStory(
        num=7,
        region="oceania",
        kicker="VANUATU · SEISMIC",
        tag="CONFIRMED",
        headline_html='<span class="num-sans">M 6.5</span> deep quake hits Vanuatu; no tsunami',
        deck="USGS logs deep South Pacific quake at 02:41 UTC; no tsunami alert.",
        source="USGS · AP",
    ),
    FeatureStory(
        num=8,
        region="oceania",
        kicker="WELLINGTON · CRICKET",
        tag="OFFICIAL",
        headline_html="New Zealand bat out Day 5 draw vs India",
        deck="Hosts reach 239 for 5 in second innings to clinch draw at Wellington.",
        source="ICC · Al Jazeera",
    ),
    FeatureStory(
        num=9,
        region="s_america",
        kicker="QUITO · ECONOMY",
        tag="OFFICIAL",
        headline_html='<span class="num-sans">IMF</span> clears <span class="num-sans">$377m</span> Ecuador loan tranche',
        deck="Board approves Ecuador loan tranche alongside $703m climate resilience deal.",
        source="IMF · Reuters",
    ),
    FeatureStory(
        num=10,
        region="africa",
        kicker="KENYA · DRC DIPLOMACY",
        tag="OFFICIAL",
        headline_html="Kenya &amp; DRC agree to restore ambassadors",
        deck="Kenyan and Congolese leaders agree to reopen embassies at regional summit.",
        source="AA · KBC",
    ),
    FeatureStory(
        num=11,
        region="east_asia",
        kicker="EAST SEA · DEFENCE",
        tag="OFFICIAL",
        headline_html="South Korea scrambles jets near Russian planes",
        deck="South Korean fighters respond off the east coast; brief island alert ends safely.",
        source="Al Jazeera",
    ),
    FeatureStory(
        num=12,
        region="middle_east",
        kicker="ABU DHABI · CRYPTO",
        tag="OFFICIAL",
        headline_html='<span class="num-sans">ADGM</span> orders 18 crypto firms to freeze tokens',
        deck="Abu Dhabi court preserves hack-linked assets across 18 crypto groups before Dec 1.",
        source="Reuters · ADGM",
    ),
    FeatureStory(
        num=13,
        region="africa",
        kicker="EAST AFRICA · SPORT",
        tag="OFFICIAL",
        headline_html='<span class="num-sans">CAF</span> signs Coca-Cola sponsor for <span class="num-sans">AFCON 2027</span>',
        deck="Partnership backs tournament co-hosted by Kenya, Tanzania &amp; Uganda.",
        source="CAF · BBC",
    ),
]

BRIEF_COL_A: List[BriefStory] = [
    BriefStory(14, "europe", "Zaporizhzhia:", "Strike on flats reportedly kills 2, hurts 40+.", "REPORTED", "AP"),
    BriefStory(15, "europe", "NATO Berlin:", "Rutte &amp; Chancellor Merz meet on defence.", "OFFICIAL", "Reuters"),
    BriefStory(16, "europe", "European Markets:", "London FTSE +1.30%; Euro Stoxx +1.92%.", "CONFIRMED", "Reuters"),
    BriefStory(17, "europe", "Premier League:", "Brentford defeat Everton 4–0 on Monday.", "OFFICIAL", "Guardian"),
    BriefStory(18, "world_space", "Oil &amp; Crypto:", "WTI crude -4.4% near $81; Bitcoin $61,200.", "CONFIRMED", "Reuters"),
    BriefStory(19, "world_space", "WTO Food Talks:", "UN food panel opens 30th session on El Nino.", "OFFICIAL", "WTO"),
    BriefStory(20, "world_space", "APAC AI Study:", "BCG reports 85% AI uptake across firms.", "REPORTED", "BCG"),
    BriefStory(21, "oceania", "Australia AI:", "Canberra flags frontier AI security threat.", "REPORTED", "Reuters"),
    BriefStory(22, "s_america", "Colombia Drone:", "Police drone attack hurts 3 &amp; hits 60+ homes.", "REPORTED", "AP"),
    BriefStory(23, "n_america", "Hawaii Volcano:", "Kilauea pauses lava flow; USGS cuts alert.", "CONFIRMED", "USGS"),
    BriefStory(24, "n_america", "NFL Result:", "Commanders edge Cincinnati Bengals 22–20.", "OFFICIAL", "AP"),
]

BRIEF_COL_B: List[BriefStory] = [
    BriefStory(25, "n_america", "NBA Basketball:", "Lakers defeat Utah Jazz 109–94 in Los Angeles.", "OFFICIAL", "AP"),
    BriefStory(26, "east_asia", "Asia Markets:", "Seoul Kospi falls 3.31%; Tokyo closed (holiday).", "CONFIRMED", "Reuters"),
    BriefStory(27, "east_asia", "China Court:", "Espionage ruling noted; child wards added.", "OFFICIAL", "Guardian"),
    BriefStory(28, "east_asia", "Japan Nuclear:", "Resident briefing opens on waste site survey.", "REPORTED", "Kyodo"),
    BriefStory(29, "south_se_asia", "India–Nepal:", "Delhi pledges $1.8bn rail &amp; energy aid pact.", "OFFICIAL", "Reuters"),
    BriefStory(30, "south_se_asia", "Indonesia ADB:", "Clears $500m clean-energy &amp; EV transition loan.", "OFFICIAL", "ADB"),
    BriefStory(31, "africa", "Nigeria Windfall:", "Study puts fossil-fuel gain at $7.5bn net.", "REPORTED", "CREA"),
    BriefStory(32, "middle_east", "Iran Claim:", "Judiciary cites $290 billion in damage rulings.", "CLAIM", "Reuters", inline_tag=True),
    BriefStory(33, "africa", "DRC Plane:", "Cessna 208 lost; rebels claim shootdown.", "CLAIM", "AFP", inline_tag=True),
    BriefStory(34, "africa", "Nigeria Attacks:", "64 reportedly dead in Niger State; troops sent.", "REPORTED", "Reuters"),
    BriefStory(35, "africa", "Morocco Finance:", "Bank opens Rabat workshop for small firms.", "OFFICIAL", "AfDB"),
]

# Coordinates in SVG viewBox 0 0 360 172 (pairwise distance strictly >= 25px)
MAP_PINS: List[Tuple[int, str, float, float]] = [
    (1, "europe", 190.0, 26.0),       # Brussels
    (2, "middle_east", 242.0, 56.0),  # Iran / Gulf
    (3, "europe", 236.0, 28.0),       # Perm, Russia
    (4, "world_space", 162.0, 44.0),  # Europe / Space Copernicus
    (5, "middle_east", 204.0, 62.0),  # Gaza / Levant
    (6, "s_america", 114.0, 78.0),    # Villavicencio, Colombia
    (7, "oceania", 342.0, 122.0),     # Vanuatu
    (8, "oceania", 342.0, 150.0),     # Wellington, NZ
    (9, "s_america", 90.0, 121.0),    # Ecuador
    (10, "africa", 204.0, 108.0),     # Kenya / DRC
    (11, "east_asia", 306.0, 52.0),   # East Sea / Korea
    (12, "middle_east", 242.0, 83.0), # Abu Dhabi
    (13, "africa", 228.0, 123.0),     # East Africa
]

EXCLUSION_TEXT = (
    "Every story above happened or was first reported on Mon 23 Nov 2026. "
    "Left out: COP31 Antalya collapse (Sun 22 Nov) · 186-drone Kyiv strike (Sun 22 Nov) · "
    "Las Vegas GP &amp; ATP Finals (Sun 22 Nov) · Khartoum UN hit (Sun 22 Nov) · "
    "ESA Euclid telescope (Tue 24 Nov)."
)

EPISTEMIC_KEY = (
    "HOW SURE: CONFIRMED = 2+ outlets · OFFICIAL = on record · "
    "REPORTED = single wire/local · CLAIM = one side's account · Vector scenes"
)

SOURCES_CREDIT = (
    "Sources: Reuters, AP, BBC, Al Jazeera, Guardian, US Treasury, IMF, USGS, UNRWA, ICC"
)


def compute_region_counts() -> Dict[str, int]:
    counts: Dict[str, int] = {r["id"]: 0 for r in REGIONS}
    all_items = [*HERO_STORIES, *MID_STORIES, *BRIEF_COL_A, *BRIEF_COL_B]
    for item in all_items:
        counts[item.region] += 1
    return counts


def validate_dataset() -> int:
    all_items = [*HERO_STORIES, *MID_STORIES, *BRIEF_COL_A, *BRIEF_COL_B]
    nums = [item.num for item in all_items]
    assert nums == list(range(1, 36)), f"Expected 1..35, got {nums}"
    counts = compute_region_counts()
    for reg in REGIONS:
        rid = str(reg["id"])
        exp = int(reg["expected"])
        got = counts[rid]
        assert got == exp, f"Region {rid}: expected {exp}, got {got}"
    assert sum(counts.values()) == 35
    return len(all_items)
