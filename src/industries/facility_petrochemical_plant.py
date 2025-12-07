from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_petrochemical_plant",
    accept_cargos_with_input_ratios=[
        ("SULP", 6),
        ("PETR", 4),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ENOL", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_FACILITY_PETROCHEMICAL_PLANT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="30",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)

industry.add_tile(
    id="facility_petrochemical_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_horizontal_tanks = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_frac_columns = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_drop_tower_and_thin_chimney = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_large_building = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_fat_chimney = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
spriteset_extra_pipe_huts_rear = industry.add_spriteset(
    sprites=[(360, 10, 64, 114, -31, -83)],
)
spriteset_extra_pipe_huts_front = industry.add_spriteset(
    sprites=[(430, 10, 64, 114, -31, -83)],
)
spriteset_extra_tanks = industry.add_spriteset(
    sprites=[(500, 10, 64, 114, -31, -83)],
)
spriteset_spherical_tanks = industry.add_spriteset(
    sprites=[(10, 140, 64, 66, -31, -35)],
)
spriteset_vertical_tanks = industry.add_spriteset(
    sprites=[(80, 140, 64, 66, -31, -35)],
)
spriteset_barrels = industry.add_spriteset(
    sprites=[(150, 140, 64, 66, -31, -35)],
    always_draw=True,
)
spriteset_salt_handling = industry.add_spriteset(
    sprites=[(220, 140, 64, 66, -31, -35)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=81,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=-1,
    zoffset=45,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=3,
    zoffset=45,
)
sprite_smoke_4 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=-1,
    zoffset=45,
)
sprite_smoke_5 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=3,
    zoffset=45,
)
sprite_smoke_6 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=0,
    zoffset=60,
)
sprite_smoke_7 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=3,
    zoffset=60,
)
sprite_smoke_8 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=3,
    yoffset=0,
    zoffset=60,
)
sprite_smoke_9 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=3,
    yoffset=3,
    zoffset=60,
)

spriteset_1_0 = industry.add_spriteset(
    sprites=[(10, 230, 64, 66, -31, -35)],
)
spriteset_2_0 = industry.add_spriteset(
    sprites=[(80, 230, 64, 128, -31, -96)],
)
spriteset_3_0 = industry.add_spriteset(
    sprites=[(150, 230, 64, 128, -31, -96)],
)
spriteset_4_0 = industry.add_spriteset(
    sprites=[(220, 230, 64, 128, -31, -96)],
)
spriteset_5_0 = industry.add_spriteset(
    sprites=[(290, 230, 64, 66, -31, -35)],
)


industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_horizontal_tanks",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_horizontal_tanks],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_frac_columns",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_frac_columns],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_drop_tower_and_thin_chimney",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_drop_tower_and_thin_chimney],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_large_building",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_large_building],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_3, sprite_smoke_4, sprite_smoke_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_fat_chimney",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_fat_chimney],
    smoke_sprites=[sprite_smoke_6, sprite_smoke_7, sprite_smoke_8, sprite_smoke_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_spherical_tanks",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_spherical_tanks],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_vertical_tanks",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_vertical_tanks],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_barrels",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_barrels],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_extra_pipe_huts_front",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_front],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_extra_pipe_huts_rear",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_rear],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_extra_tanks",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_tanks],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_salt_handling",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_salt_handling],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_empty",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)

industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_1",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1_0],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_2",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2_0],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_3",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3_0],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_4",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4_0],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_petrochemical_plant_spritelayout_5",
    tile="facility_petrochemical_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5_0],
    fences=["nw", "ne", "se", "sw"],
)


industry.add_industry_layout(
    id="facility_petrochemical_plant_industry_layout_1",
    layout=[
        (0, 0, "facility_petrochemical_plant_spritelayout_drop_tower_and_thin_chimney"),
        (0, 1, "facility_petrochemical_plant_spritelayout_4"),
        (1, 0, "facility_petrochemical_plant_spritelayout_large_building"),
        (1, 1, "facility_petrochemical_plant_spritelayout_4"),
        (2, 0, "facility_petrochemical_plant_spritelayout_frac_columns"),
        (2, 1, "facility_petrochemical_plant_spritelayout_4"),
    ],
)
