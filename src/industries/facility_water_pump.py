from industry import IndustryPrimaryNoSupplies, TileLocationChecks

industry = IndustryPrimaryNoSupplies(
    id="facility_water_pump",
    prod_cargo_types_with_multipliers=[
        ("WATR", 8),
    ],
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="151",
    colour_scheme_name="scheme_3_hendrix",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    name="string(STR_IND_FACILITY_WATER_PUMP)",
    fund_cost_multiplier="15",
    nearby_station_name="string(STR_STATION_WELLS)",
    pollution_and_squalor_factor=1,
    provides_snow=False,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

industry.add_tile(
    id="facility_water_pump_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="facility_water_pump_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
) 
spriteset_jetty_left = industry.add_spriteset(
    sprites=[(10, 153, 64, 39, -31, -7)],
    always_draw=True,
)
spriteset_jetty_right = industry.add_spriteset(
    sprites=[(80, 153, 64, 39, -31, -7)], always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 153, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 153, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 153, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 153, 64, 39, -31, -7)],
)


industry.add_spritelayout(
    id="facility_water_pump_spritelayout_left",
    tile="facility_water_pump_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_jetty_left, spriteset_small_tanks],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="facility_water_pump_spritelayout_right",
    tile="facility_water_pump_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_jetty_right, spriteset_small_tanks],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="facility_water_pump_spritelayout_both",
    tile="facility_water_pump_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[
        spriteset_jetty_left,
        spriteset_jetty_right,
        spriteset_small_tanks,
    ],
    terrain_aware_ground=True,
)



industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="facility_water_pump_spritelayout_coast",
    tile="facility_water_pump_tile_2",
    config={
        "ground_sprite": None,
        "building_sprites": [spriteset_small_tanks],
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

industry.add_industry_layout(
    id="facility_water_pump_industry_layout_1",
    layout=[
        (0, 0, "facility_water_pump_spritelayout_coast"),
        (0, 1, "facility_water_pump_spritelayout_right"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "facility_water_pump_spritelayout_coast"),
        (1, 1, "facility_water_pump_spritelayout_both"),
        (1, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (1, 0, "facility_water_pump_spritelayout_both"),
        (1, 1, "facility_water_pump_spritelayout_right"),
        (2, 0, "facility_water_pump_spritelayout_coast"),
        (2, 1, "facility_water_pump_spritelayout_coast"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_3",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "facility_water_pump_spritelayout_both"),
        (0, 2, "facility_water_pump_spritelayout_coast"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "facility_water_pump_spritelayout_left"),
        (1, 2, "facility_water_pump_spritelayout_coast"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_4",
    layout=[
        (0, 0, "facility_water_pump_spritelayout_coast"),
        (0, 1, "facility_water_pump_spritelayout_coast"),
        (1, 0, "facility_water_pump_spritelayout_both"),
        (1, 1, "facility_water_pump_spritelayout_right"),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "spritelayout_null_water"),
    ],
)
