from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="refinery_salvage",
    accept_cargos_with_input_ratios=[
        ("SALV", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("BMAT", 5),
        ("DIES", 1),
        ("EXPW", 2),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="3",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_REF_SALV)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="255",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
    locate_in_specific_biomes=[
        "exclude_map_edges",
    ],
)


spriteset_ground = industry.add_spriteset(
    type="pavement",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="refinery_salvage_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="refinery_salvage_industry_layout",
    layout=[(0, 0, "refinery_salvage_spritelayout")],
)
