from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_coal_refinery",
    accept_cargos_with_input_ratios=[
        ("COAL", 5),
        ("WATR", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("COKE", 6),
        ("SULP", 1),
        ("OIL_", 1),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="10",
    colour_scheme_name="scheme_2_dylan", # cabbage needs checked
    name="string(STR_IND_FACILITY_COAL_REFINERY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="2",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)
industry.add_tile(
    id="facility_coal_refinery_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


sprite_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_silo = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery_larry_car = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
)
spriteset_pusher_rails_base = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)], yextent=8  # prevents gantry flickering ??
)
spriteset_pusher_car = industry.add_spriteset(
    sprites=[(10, 234, 64, 64, -31, -32)], yextent=8  # prevents gantry flickering ??
)
spriteset_pipe_gantry = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_front = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_rear = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_quench_tower = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
spriteset_gas_plant_1 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -91)],
)
spriteset_extra_pipe_huts_rear = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -91)],
)
spriteset_extra_pipe_huts_front = industry.add_spriteset(
    sprites=[(780, 10, 64, 122, -31, -91)],
)
spriteset_tile_tar_tanks = industry.add_spriteset(
    sprites=[(850, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_angled = industry.add_spriteset(
    sprites=[(920, 10, 64, 122, -31, -91)],
)
spriteset_extra_coal_front = industry.add_spriteset(
    sprites=[(990, 10, 64, 122, -31, -91)],
)
spriteset_extra_coal_rear = industry.add_spriteset(
    sprites=[(1060, 10, 64, 122, -31, -91)],
)
spriteset_mostly_empty = industry.add_spriteset(
    sprites=[(1130, 10, 64, 122, -31, -91)],
)
sprite_smoke_big_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=8,
    yoffset=5,
    zoffset=104,
)
sprite_smoke_big_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=7,
    zoffset=76,
)
sprite_smoke_small_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=0,
    zoffset=16,
)
sprite_smoke_small_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=5,
    zoffset=16,
)

industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_empty",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_oven_battery_pipes_only",
    # tile id has to match larry car spritelayout for the multiple-view object case
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_oven_battery],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_oven_battery_larry_car",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_oven_battery_larry_car],
    smoke_sprites=[sprite_smoke_small_1, sprite_smoke_small_2],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_silo",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_silo],
    smoke_sprites=[sprite_smoke_big_1],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_pusher_rails_empty",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_pusher_rails_with_car",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[
        spriteset_pusher_rails_base,
        spriteset_pusher_car,
        spriteset_pipe_gantry,
    ],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_pusher_rails_with_house",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry_house],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_quench_tower",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_quench_tower],
    smoke_sprites=[sprite_smoke_big_2],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_gas_plant_1",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_gas_plant_1],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_coal_handling_front",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_coal_handling_front],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_coal_handling_rear",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_coal_handling_rear],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_coal_front",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_coal_front],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_coal_rear",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_coal_rear],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_pipe_huts_front",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_front],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_pipe_huts_rear",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_extra_pipe_huts_rear],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_tar_tanks",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tile_tar_tanks],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_pipe_gantry_plain",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pipe_gantry],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_extra_pipe_gantry_fancy",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_pipe_gantry_angled],
)
industry.add_spritelayout(
    id="facility_coal_refinery_spritelayout_mostly_empty",
    tile="facility_coal_refinery_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_mostly_empty],
)


industry.add_industry_layout(
    id="facility_coal_refinery_industry_layout_1",
    layout=[
        (0, 0, "facility_coal_refinery_spritelayout_silo"),
        (0, 1, "facility_coal_refinery_spritelayout_coal_handling_rear"),
        (0, 2, "facility_coal_refinery_spritelayout_extra_coal_rear"),
        (1, 0, "facility_coal_refinery_spritelayout_quench_tower"),
        (1, 1, "facility_coal_refinery_spritelayout_coal_handling_front"),
        (1, 2, "facility_coal_refinery_spritelayout_extra_coal_front"),
        (2, 0, "facility_coal_refinery_spritelayout_extra_pipe_gantry_fancy"),
        (2, 1, "facility_coal_refinery_spritelayout_gas_plant_1"),
    ],
)