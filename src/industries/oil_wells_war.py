from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="oil_wells_war",
    accept_cargos_with_input_ratios=[
        ("WATR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("OIL_", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="7",
    map_colour="151",
    colour_scheme_name="scheme_1_elton",
    name="TTD_STR_INDUSTRY_NAME_OIL_WELLS",
    nearby_station_name="string(STR_STATION_WELLS)",
    fund_cost_multiplier="252",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)
industry.enable_in_economy(
    "WAR_ECONOMY",
    prob_map_gen="4",
)


spriteset_ground = industry.add_spriteset(
    type="pavement",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="oil_wells_war_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="oil_wells_war_industry_layout",
    layout=[(0, 0, "oil_wells_war_spritelayout")],
)
