from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="refinery_sulphur",
    accept_cargos_with_input_ratios=[
        ("SULP", 40),
    ],
    prod_cargo_types_with_output_ratios=[
        ("HEPW", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="3",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_REF_SULPH)",
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

industry.add_tile(
    id="refinery_sulphur_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="pavement",
)

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 161, 64, 78, -31, -50)],
)

spriteset_2 = industry.add_spriteset(
    sprites=[(81, 161, 64, 70, -31, -46)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -31, -54)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(441, 410, 64, 84, -31, -54)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(251, 505, 64, 31, -31, -20)],
)

industry.add_spritelayout(
    id="refinery_sulphur_spritelayout_1",
    tile="refinery_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="refinery_sulphur_spritelayout_2",
    tile="spriteset_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="refinery_sulphur_industry_layout_1",
    layout=[
        (0, 0, "refinery_sulphur_spritelayout_1"),
        (1, 0, "refinery_sulphur_spritelayout_2"),
    ],
)

