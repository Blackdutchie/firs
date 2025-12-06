from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_forge",
    accept_cargos_with_input_ratios=[
        ("COKE", 6),
        ("SALV", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("BASS", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_FACILITY_FORGE)",
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


industry.add_tile(
    id="facility_forge_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_tanks = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_tanks_ground_shading = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_furnace = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_caster = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_metal_with_small_train_car_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -90)],
)
spriteset_metal_3 = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -90)],
)
spriteset_metal_4 = industry.add_spriteset(
    sprites=[(780, 10, 64, 122, -31, -90)],
)
spriteset_high_tower = industry.add_spriteset(
    sprites=[(500, 860, 64, 122, -31, -90)],
)



sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=61,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=4,
    yoffset=1,
    zoffset=93,
)



industry.add_spritelayout(
    id="facility_forge_spritelayout_empty",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_tanks",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_tanks_ground_shading,
    building_sprites=[spriteset_tanks],
    fences=[],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_air_plant",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_air_plant],
    smoke_sprites=[sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_furnace",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_furnace],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_casting_shed",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_caster],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_metal_with_small_train_car_1",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_metal_with_small_train_car_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_small_shed",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_shed],
    fences=["nw", "se"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_metal_1",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_metal_2",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_metal_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_metal_3",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_metal_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="facility_forge_spritelayout_metal_4",
    tile="facility_forge_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_metal_4],
    fences=["nw", "ne", "se", "sw"],
)



industry.add_industry_layout(
    id="facility_forge_industry_layout_1",
    layout=[
        (0, 0, "facility_forge_spritelayout_casting_shed"),
        (0, 1, "facility_forge_spritelayout_furnace"),
        (1, 0, "facility_forge_spritelayout_furnace"),
        (1, 1, "facility_forge_spritelayout_air_plant"),
        (2, 0, "facility_forge_spritelayout_casting_shed"),
        (2, 1, "facility_forge_spritelayout_small_shed"),
    ],
)