from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="mine_sulphur",
    accept_cargos_with_input_ratios=[
        ("DIES", 6),
        ("PETR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("SULP", 4),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="3",
    map_colour="194",
    colour_scheme_name="scheme_13_whitney", # cabbage needs checked
    name="string(STR_IND_MINE_SULPHUR)",
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
    id="mine_sulphur_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_hut_vents = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_ore_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
    always_draw=True,
)
spriteset_ore_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
    always_draw=True,
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_exit_shed_rear = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_exit_shed_front = industry.add_spriteset(
    sprites=[(360, 160, 64, 122, -31, -90)],
)
spriteset_belt_tower = industry.add_spriteset(
    sprites=[(10, 310, 64, 122, -31, -90)],
)

sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=-1,
    yoffset=2,
    zoffset=38,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=-1,
    yoffset=6,
    zoffset=38,
)

industry.add_spritelayout(
    id="mine_sulphur_spritelayout_tile_empty",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)

industry.add_spritelayout(
    id="mine_sulphur_spritelayout_crusher_front_part",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_front_part],
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_crusher_rear_part",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_rear_part],
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_hut_vents",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_hut_vents],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_ore_1",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_ore_1],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_ore_2",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_ore_2],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_empty",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_winding_house",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_winding_house],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_exit_shed_rear",
    # tile has to match trestle for multi-tile object case
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_exit_shed_rear],
)

industry.add_spritelayout(
    id="mine_sulphur_spritelayout_exit_shed_front",
    # tile has to match trestle for multi-tile object case
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_exit_shed_front],
)
industry.add_spritelayout(
    id="mine_sulphur_spritelayout_belt_tower",
    tile="mine_sulphur_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_belt_tower],
    add_to_object_num=6,
)

industry.add_industry_layout(
    id="mine_sulphur_industry_layout_1",
    layout=[
        (0, 0, "mine_sulphur_spritelayout_belt_tower"),
        (0, 1, "mine_sulphur_spritelayout_exit_shed_rear"),
        (1, 0, "mine_sulphur_spritelayout_crusher_rear_part"),
        (1, 1, "mine_sulphur_spritelayout_exit_shed_front"),
        (1, 2, "mine_sulphur_spritelayout_ore_1"),
        (2, 0, "mine_sulphur_spritelayout_crusher_front_part"),
        (2, 1, "mine_sulphur_spritelayout_ore_2"),
    ],
)

industry.add_industry_layout(
    id="mine_sulphur_industry_layout_2",
    layout=[
        (0, 0, "mine_sulphur_spritelayout_belt_tower"),
        (0, 1, "mine_sulphur_spritelayout_exit_shed_rear"),
        (0, 2, "mine_sulphur_spritelayout_crusher_rear_part"),
        (1, 0, "mine_sulphur_spritelayout_ore_1"),
        (1, 1, "mine_sulphur_spritelayout_exit_shed_front"),
        (1, 2, "mine_sulphur_spritelayout_crusher_front_part"),
        (2, 1, "mine_sulphur_spritelayout_ore_2"),
    ],
)