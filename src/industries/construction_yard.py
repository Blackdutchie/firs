from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="construction_yard",
    accept_cargos_with_input_ratios=[
        ("BMAT", 16),
    ],
    prod_cargo_types_with_output_ratios=[
        ("SHIP", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="45",
    map_colour="141",
    colour_scheme_name="scheme_7_bowie", # cabbage needs checked
    name="string(STR_IND_CONSTRUCTION_YARD)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="255",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)
industry.add_tile(
    id="construction_yard_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)

spriteset_8 = industry.add_spriteset(
    sprites=[(80, 146, 64, 84, -31, -54)],
)


industry.add_spritelayout(
    id="construction_yard_spritelayout_empty",
    tile="construction_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="construction_yard_spritelayout_8",
    tile="construction_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)


industry.add_industry_layout(
    id="construction_yard_industry_layout_1",
    layout=[
        (0, 0, "construction_yard_spritelayout_empty"),
        (0, 1, "construction_yard_spritelayout_empty"),
        (1, 0, "construction_yard_spritelayout_empty"),
        (1, 1, "construction_yard_spritelayout_empty"),
        (1, 2, "construction_yard_spritelayout_8"),
    ],
)
