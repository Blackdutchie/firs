from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_engineering_bay",
    accept_cargos_with_input_ratios=[
        ("COKE", 8),
        ("PCMT", 4),
        ("ENOL", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("AASS", 4),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_FACILITY_ENGINEERING_BAY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="30",
    pollution_and_squalor_factor=1,
    sprites_complete=False,
    animated_tiles_fixed=False,
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
    id="facility_engineering_bay_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="facility_engineering_bay_industry_layout",
    layout=[(0, 0, "facility_engineering_bay_spritelayout")],
)
