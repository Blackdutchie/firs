from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="seaport",
    accept_cargos_with_input_ratios=[
        ("VEHI", 1),
        ("ITEM", 4),
        ("SHIP", 1),
        ("ARTY", 1),
        ("AVEH", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FRNT", 8),
    ],
    prob_in_game="0",
    prob_map_gen="4",
    # map_colour="186", # former orange before v5?
    # map_colour="177",  # former Bulk Terminal colour?
    map_colour="45",
    colour_scheme_name="scheme_9_shania",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    name="string(STR_IND_SEAPORT)",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_2)",
    fund_cost_multiplier="255",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)


industry.add_tile(
    id="seaport_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="seaport_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)

spriteset_jetty_left = industry.add_spriteset(
    sprites=[(10, 232, 64, 39, -31, -7)],
    always_draw=True,
)
spriteset_jetty_right = industry.add_spriteset(
    sprites=[(80, 232, 64, 39, -31, -7)], always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 232, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 232, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 232, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 232, 64, 39, -31, -7)],
)

spriteset_boat_nw_se = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -31, -7)],
)
spriteset_boat_ne_sw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -7)],
)
spriteset_boat_se_nw = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -7)],
)
spriteset_boat_sw_ne = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -31, -7)],
)

spriteset_crane_BR = industry.add_spriteset(
    sprites=[(440, 410, 64, 84, -34, -53)],
)
spriteset_crane_BL = industry.add_spriteset(
    sprites=[(510, 410, 64, 84, -34, -53)],
)
spriteset_crane_TR = industry.add_spriteset(
    sprites=[(580, 410, 64, 84, -34, -53)],
)
spriteset_crane_TL = industry.add_spriteset(
    sprites=[(650, 410, 64, 84, -34, -53)],
)
spriteset_shed_full_nw_se = industry.add_spriteset(
    sprites=[(720, 210, 64, 84, -31, -61)],
)
spriteset_shed_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 210, 64, 84, -31, -61)],
)

industry.add_spritelayout(
    id="seaport_spritelayout_water_empty",
    tile="seaport_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[
        spriteset_jetty_left,
        spriteset_jetty_right,
    ],
    terrain_aware_ground=True,
)



industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="seaport_spritelayout_coast_empty",
    tile="seaport_tile_2",
    config={
        "ground_sprite": spriteset_ground,
        "building_sprites": [],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_right,
            "se_nw": spriteset_jetty_left,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="seaport_spritelayout_coast_crane_BR",
    tile="seaport_tile_2",
    config={
        "ground_sprite": spriteset_ground,
        "building_sprites": [spriteset_crane_BR],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_right,
            "se_nw": spriteset_jetty_left,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="seaport_spritelayout_coast_crane_BL",
    tile="seaport_tile_2",
    config={
        "ground_sprite": spriteset_ground,
        "building_sprites": [spriteset_crane_BL],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_right,
            "se_nw": spriteset_jetty_left,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="seaport_spritelayout_coast_crane_TR",
    tile="seaport_tile_2",
    config={
        "ground_sprite": spriteset_ground,
        "building_sprites": [spriteset_crane_TR],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_right,
            "se_nw": spriteset_jetty_left,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="seaport_spritelayout_coast_crane_TL",
    tile="seaport_tile_2",
    config={
        "ground_sprite": spriteset_ground,
        "building_sprites": [spriteset_crane_TL],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_right,
            "se_nw": spriteset_jetty_left,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)



industry.add_spritelayout(
    id="seaport_spritelayout_shed_nw_se",
    tile="seaport_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[
        spriteset_jetty_left,
        spriteset_jetty_right,
        spriteset_shed_full_nw_se,
    ],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="seaport_spritelayout_shed_ne_sw",
    tile="seaport_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[
        spriteset_jetty_left,
        spriteset_jetty_right,
        spriteset_shed_full_ne_sw,
    ],
    terrain_aware_ground=True,
)




industry.add_industry_layout(
    id="seaport_industry_layout_1",
    layout=[
        (0, 0, "seaport_spritelayout_coast_crane_BL"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "seaport_spritelayout_coast_empty"),
        (1, 1, "seaport_spritelayout_water_empty"),
        (1, 2, "seaport_spritelayout_shed_nw_se"),
        (1, 3, "spritelayout_null_water"),
        (2, 0, "seaport_spritelayout_coast_empty"),
        (2, 1, "seaport_spritelayout_water_empty"),
        (2, 2, "seaport_spritelayout_shed_nw_se"),
        (2, 3, "spritelayout_null_water"),
        (3, 0, "seaport_spritelayout_coast_crane_TR"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="seaport_industry_layout_2",
    layout=[
        (0, 0, "seaport_spritelayout_coast_crane_BR"),
        (0, 1, "seaport_spritelayout_coast_empty"),
        (0, 2, "seaport_spritelayout_coast_empty"),
        (0, 3, "seaport_spritelayout_coast_crane_TL"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "seaport_spritelayout_water_empty"),
        (1, 2, "seaport_spritelayout_water_empty"),
        (1, 3, "spritelayout_null_water"),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "seaport_spritelayout_shed_ne_sw"),
        (2, 2, "seaport_spritelayout_shed_ne_sw"),
        (2, 3, "spritelayout_null_water"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="seaport_industry_layout_3",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (0, 3, "seaport_spritelayout_coast_crane_BL"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "seaport_spritelayout_shed_nw_se"),
        (1, 2, "seaport_spritelayout_water_empty"),
        (1, 3, "seaport_spritelayout_coast_empty"),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "seaport_spritelayout_shed_nw_se"),
        (2, 2, "seaport_spritelayout_water_empty"),
        (2, 3, "seaport_spritelayout_coast_empty"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
        (3, 3, "seaport_spritelayout_coast_crane_TR"),
    ],
)
industry.add_industry_layout(
    id="seaport_industry_layout_4",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "seaport_spritelayout_shed_ne_sw"),
        (1, 2, "seaport_spritelayout_shed_ne_sw"),
        (1, 3, "spritelayout_null_water"),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "seaport_spritelayout_water_empty"),
        (2, 2, "seaport_spritelayout_water_empty"),
        (2, 3, "spritelayout_null_water"),
        (3, 0, "seaport_spritelayout_coast_crane_BR"),
        (3, 1, "seaport_spritelayout_coast_empty"),
        (3, 2, "seaport_spritelayout_coast_empty"),
        (3, 3, "seaport_spritelayout_coast_crane_TL"),
    ],
)