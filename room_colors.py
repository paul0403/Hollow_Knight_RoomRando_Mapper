# Note: some rooms do not follow the general naming scheme
# e.g. The room in Queen's Gardens that lead down to Deepnest is "Deepnest_43"
# We just ignore them now. Geographically, these rooms are close enough to their canonical color

from functools import lru_cache


def get_room_and_text_color(room_name):
    room_color = _impl_get_room_and_text_color(room_name)
    return room_color, _get_contrast_color(room_color)


@lru_cache(maxsize=512)
def _impl_get_room_and_text_color(room_name: str) -> str:

    # Basin and Abyss
    if room_name.startswith("Abyss") and not (
        room_name
        in (
            "Abyss_01",
            "Abyss_03_c",
        )
    ):
        return "#2E2E2E"

    # City
    if (
        room_name.startswith(("Ruins1", "Ruins2")) and not (room_name in ("Ruins2_10"))
    ) or room_name in (
        "Abyss_01",
        "Crossroads_49b",
    ):
        return "#7479AA"

    # Crystal Peak
    if room_name.startswith("Mines"):
        return "#CFA9CD"

    # Deepnest
    if (
        room_name.startswith("Deepnest")
        and not room_name.startswith("Deepnest_East")
        and not (room_name in ("Deepnest_01", "Deepnest_43"))
    ):
        return "#676F7F"

    # Howling cliffs, Dirtmouth, King's Pass
    if room_name.startswith("Cliffs") or room_name in (
        "Fungus1_28",
        "Town",
        "Tutorial_01",
    ):
        return "#202020"

    # Fog Canyon
    if room_name in (
        "Fungus3_44",
        "Fungus3_30",
        "Fungus3_24",
        "Fungus3_01",
        "Fungus3_03",
        "Fungus3_02",
        "Fungus3_35",
        "Fungus3_25",
        "Fungus3_47",
        "Fungus3_28",
        "Fungus3_25b",
        "Fungus3_27",
        "Fungus3_26",
    ):
        return "#F1C7E6"

    # Crossroads
    if room_name.startswith("Crossroads") and not (
        room_name
        in (
            "Crossroads_50",
            "Crossroads_46b",
        )
    ):
        return "#A5CFE8"

    # Fungal wastes
    if room_name.startswith("Fungus2") or room_name in ("Deepnest_01",):
        return "#DFE9C0"

    # Greenpath
    if room_name.startswith("Fungus1") and not (
        room_name
        in (
            "Fungus1_23",
            "Fungus1_24",
        )
    ):
        return "#C0F7BE"

    # Kingdom's edge
    if room_name.startswith("Deepnest_East") or room_name in (
        "Abyss_03_c",
        "GG_Lurker",
    ):
        return "#998F86"

    # Queen's Gardens
    if room_name in (
        "Fungus3_48",
        "Fungus3_40",
        "Fungus3_39",
        "Fungus1_23",
        "Fungus3_23",
        "Fungus3_22",
        "Fungus3_21",
        "Fungus3_13",
        "Fungus3_10",
        "Fungus3_08",
        "Fungus3_50",
        "Deepnest_43",
        "Fungus3_39",
        "Fungus3_11",
        "Fungus3_05",
        "Fungus3_04",
        "Fungus3_34",
        "Fungus1_24",
    ):
        return "#7A9B82"

    # Resting Grounds
    if room_name.startswith("RestingGrounds") or room_name in (
        "Crossroads_50",
        "Crossroads_46b",
        "Ruins2_10",
    ):
        return "#F1BC9C"

    # Waterways
    if room_name.startswith("Waterways") or room_name == "GG_Waterways":
        return "#84F8FE"

    # Hive
    if room_name.startswith("Hive"):
        return "#EAD794"

    # White Palace
    if room_name.startswith("White_Palace"):
        return "#CBCFD3"

    # Unchecked
    if room_name.startswith("???"):
        return "#F81003"

    # Others
    else:
        return "#FFFFFF"


@lru_cache(maxsize=32)
def _get_contrast_color(hex_color: str) -> str:
    """
    Given a hex color string (e.g., '#FFFFFF'),
    returns '#000000' (black) if the background is bright,
    or '#FFFFFF' (white) if the background is dark.

    Formula from
    https://en.wikipedia.org/wiki/Relative_luminance
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    luminance = (0.2126 * r) + (0.7152 * g) + (0.0722 * b)
    return "#000000" if luminance > 127.5 else "#FFFFFF"
