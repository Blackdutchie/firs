from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="factory_war",
    accept_cargos_with_input_ratios=[
        ("BMAT", 6),
        ("EXPW", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ITEM", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="34",
    map_colour="151",
    colour_scheme_name="scheme_3_hendrix", # cabbage needs checked
    name="string(STR_IND_FACTORY_WAR)",
    special_flags=["IND_FLAG_BUILT_NEAR_TOWN"],
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
    id="factory_war_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 101, -31, -64)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 101, -31, -59)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 101, -31, -71)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 101, -31, -69)],
)
spriteset_sand_staithe = industry.add_spriteset(
    sprites=[(290, 10, 64, 31, -31, 0)],
)
spriteset_clay_staithe = industry.add_spriteset(
    sprites=[(360, 10, 64, 31, -31, 0)],
)
sprite_smoke_boilerhouse = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=8,
    yoffset=0,
    zoffset=70,
)
sprite_smoke_kiln = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=8,
    zoffset=58,
)
industry.add_spritelayout(
    id="factory_war_spritelayout_empty",
    tile="factory_war_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_1",
    ground_sprite=spriteset_ground,
    tile="factory_war_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_boilerhouse],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_2",
    ground_sprite=spriteset_ground,
    tile="factory_war_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_3",
    ground_sprite=spriteset_ground,
    tile="factory_war_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_3],
    smoke_sprites=[sprite_smoke_kiln],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_4",
    ground_sprite=spriteset_ground,
    tile="factory_war_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_sand_staithe",
    tile="factory_war_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_sand_staithe],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="factory_war_spritelayout_clay_staithe",
    tile="factory_war_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_clay_staithe],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="factory_war_industry_layout_1",
    layout=[
        (0, 0, "factory_war_spritelayout_1"),
        (0, 1, "factory_war_spritelayout_2"),
        (0, 2, "factory_war_spritelayout_4"),
        (1, 0, "factory_war_spritelayout_2"),
        (1, 1, "factory_war_spritelayout_2"),
        (1, 2, "factory_war_spritelayout_3"),
        (2, 1, "factory_war_spritelayout_2"),
    ],
)
