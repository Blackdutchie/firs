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
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for the water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
) 

industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="facility_water_pump_spritelayout_small_tanks",
    tile="facility_water_pump_tile_1",
    config={
        "ground_sprite": None,
        "jetty_foundations": True,
        "building_sprites": {
            "slope_nw_se": [
                spriteset_small_tanks,
            ],
            "slope_ne_sw": [
                spriteset_small_tanks,
            ],
            "slope_se_nw": [
                spriteset_small_tanks,
            ],
            "slope_sw_ne": [
                spriteset_small_tanks,
            ],
        },
    },
)

industry.add_industry_layout(
    id="facility_water_pump_industry_layout_1",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "facility_water_pump_spritelayout_small_tanks"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (1, 0, "facility_water_pump_spritelayout_small_tanks"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_3",
    layout=[
        (0, 0, "facility_water_pump_spritelayout_small_tanks"),
        (0, 1, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout_4",
    layout=[
        (0, 0, "facility_water_pump_spritelayout_small_tanks"),
        (1, 0, "spritelayout_null_water"),
    ],
)
