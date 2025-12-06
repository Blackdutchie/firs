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
    provides_snow=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

spriteset_ground = industry.add_spriteset(
    type="pavement",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="facility_water_pump_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="facility_water_pump_industry_layout",
    layout=[(0, 0, "facility_water_pump_spritelayout")],
)
