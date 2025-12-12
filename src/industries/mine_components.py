from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="mine_components",
    accept_cargos_with_input_ratios=[
        ("DIES", 6),
        ("PETR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("COMP", 4),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="3",
    map_colour="164",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_MINE_COMPONENTS)",
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
    id="mine_components_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
spriteset_mine_tower = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -88)],
)

spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_misc_building = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_vents_shed = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=3,
    zoffset=16,
)


industry.add_spritelayout(
    id="mine_components_spritelayout_tile_empty",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_mine_tower",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_mine_tower],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_crusher_front_part",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_front_part],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_crusher_mid_part",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_crusher_rear_part",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crusher_rear_part],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_misc_building",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_misc_building],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_vents_shed",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_vents_shed],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mine_components_spritelayout_winding_house",
    tile="mine_components_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_winding_house],
    fences=["nw", "ne", "se", "sw"],
)


industry.add_industry_layout(
    id="mine_components_industry_layout_1",
    layout=[
        (0, 0, "mine_components_spritelayout_mine_tower"),
        (0, 1, "mine_components_spritelayout_crusher_rear_part"),
        (1, 0, "mine_components_spritelayout_mine_tower"),
        (1, 1, "mine_components_spritelayout_crusher_front_part"),
        (2, 0, "mine_components_spritelayout_winding_house"),
        (2, 1, "mine_components_spritelayout_vents_shed"),
    ],
)

industry.add_industry_layout(
    id="mine_components_industry_layout_2",
    layout=[
        (0, 0, "mine_components_spritelayout_mine_tower"),
        (0, 1, "mine_components_spritelayout_winding_house"),
        (0, 2, "mine_components_spritelayout_crusher_rear_part"),
        (1, 0, "mine_components_spritelayout_mine_tower"),
        (1, 1, "mine_components_spritelayout_vents_shed"),
        (1, 2, "mine_components_spritelayout_crusher_front_part"),
    ],
)