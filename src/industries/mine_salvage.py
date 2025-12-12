from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="mine_salvage",
    accept_cargos_with_input_ratios=[
        ("DIES", 6),
        ("PETR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("SALV", 12),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="8",
    map_colour="55",
    colour_scheme_name="scheme_3_hendrix", # cabbage needs checked
    name="string(STR_IND_MINE_SALVAGE)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="255",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)
spriteset_ground = industry.add_spriteset(
    type="gravel",
)

industry.add_tile(
    id="mine_salvage_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_tower = industry.add_spriteset(
    sprites=[(80, 310, 64, 122, -31, -88)],
)
spriteset_house_front = industry.add_spriteset(
    sprites=[(360, 160, 64, 122, -31, -88)],
)

spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_ore_truck = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_joined_ore_front = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
    always_draw=True,
)
spriteset_joined_ore_rear = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
    always_draw=True,
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_exit_shed_rear = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_boiler_house = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=6,
    zoffset=71,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=11,
    zoffset=71,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="mine_salvage_spritelayout_tile_empty",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)

industry.add_spritelayout(
    id="mine_salvage_spritelayout_crusher_front_part",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_front_part],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_crusher_rear_part",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_rear_part],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_ore_truck",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_ore_truck],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_joined_ore_front",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_joined_ore_front],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_joined_ore_rear",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_joined_ore_rear],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_boiler_house",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_boiler_house],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_winding_house",
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_winding_house],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_exit_shed_rear",
    # tile has to match trestle for multi-tile object case
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_exit_shed_rear],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_exit_shed_front",
    # tile has to match trestle for multi-tile object case
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_house_front],
)
industry.add_spritelayout(
    id="mine_salvage_spritelayout_tower",
    # tile has to match trestle for multi-tile object case
    tile="mine_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tower],
)

industry.add_industry_layout(
    id="mine_salvage_industry_layout_1",
    layout=[
        (0, 0, "mine_salvage_spritelayout_tower"),
        (0, 1, "mine_salvage_spritelayout_crusher_rear_part"),
        (1, 0, "mine_salvage_spritelayout_exit_shed_rear"),
        (1, 1, "mine_salvage_spritelayout_crusher_front_part"),
        (2, 0, "mine_salvage_spritelayout_exit_shed_front"),
        (2, 1, "mine_salvage_spritelayout_joined_ore_rear"),
        (3, 1, "mine_salvage_spritelayout_joined_ore_front"),
    ],
)

industry.add_industry_layout(
    id="mine_salvage_industry_layout_2",
    layout=[
        (0, 0, "mine_salvage_spritelayout_tower"),
        (0, 1, "mine_salvage_spritelayout_crusher_rear_part"),
        (0, 2, "mine_salvage_spritelayout_boiler_house"),
        (1, 0, "mine_salvage_spritelayout_joined_ore_rear"),
        (1, 1, "mine_salvage_spritelayout_crusher_front_part"),
        (1, 2, "mine_salvage_spritelayout_exit_shed_rear"),
        (2, 0, "mine_salvage_spritelayout_joined_ore_front"),
        (2, 2, "mine_salvage_spritelayout_exit_shed_front"),
    ],
)