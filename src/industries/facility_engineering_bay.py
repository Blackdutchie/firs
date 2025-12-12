from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_engineering_bay",
    accept_cargos_with_input_ratios=[
        ("COKE", 3),
        ("PCMT", 2),
        ("ENOL", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("AASS", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="10",
    colour_scheme_name="scheme_2_dylan", # cabbage needs checked
    name="string(STR_IND_FACILITY_ENGINEERING_BAY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="8",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

spriteset_ground = industry.add_spriteset(
    type="pavement",
)

industry.add_tile(
    id="facility_engineering_bay_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 113, -31, -82)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 113, -31, -82)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(220, 10, 64, 113, -31, -82)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(290, 10, 64, 113, -31, -82)],
)

spriteset_6 = industry.add_spriteset(
    sprites=[(430, 10, 64, 113, -31, -82)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(500, 10, 64, 113, -31, -82)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(570, 10, 64, 113, -31, -82)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(640, 10, 64, 113, -31, -82)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(710, 10, 64, 113, -31, -82)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(780, 10, 64, 113, -31, -82)],
)
spriteset_clay_staithe = industry.add_spriteset(
    sprites=[(80, 130, 64, 31, -31, 0)],
)
spriteset_stone_staithe = industry.add_spriteset(
    sprites=[(150, 130, 64, 31, -31, 0)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=81,
    animation_frame_offset=1,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=3, yoffset=0, zoffset=81
)

industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_1",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_2",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_3",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_4",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_6",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_7",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_8",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_9",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_10",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_11",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_11],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_clay_staithe",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_clay_staithe],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_engineering_bay_spritelayout_stone_staithe",
    tile="facility_engineering_bay_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_stone_staithe],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="facility_engineering_bay_industry_layout_1",
    layout=[
        (0, 0, "facility_engineering_bay_spritelayout_2"),
        (0, 1, "facility_engineering_bay_spritelayout_3"),
        (1, 0, "facility_engineering_bay_spritelayout_4"),
        (1, 1, "facility_engineering_bay_spritelayout_1"),
        (2, 0, "facility_engineering_bay_spritelayout_11"),
        (2, 1, "facility_engineering_bay_spritelayout_8"),
        (2, 2, "facility_engineering_bay_spritelayout_7"),
        (3, 0, "facility_engineering_bay_spritelayout_10"),
        (3, 1, "facility_engineering_bay_spritelayout_9"),
    ],
)