from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_blast_furnace",
    accept_cargos_with_input_ratios=[
        ("PETR", 2),
        ("CMAT", 2),
        ("COMP", 4),
    ],
    prod_cargo_types_with_output_ratios=[
        ("PCMT", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="166",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_FACILITY_BLAST_FURNACE)",
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
    type="gravel",
)


spriteset_ground_tile_dark = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_greeble = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
)
spriteset_blast_furnace_2 = industry.add_spriteset(
    sprites=[(10, 10, 64, 144, -31, -114)],
)
spriteset_blast_furnace_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_small_shed = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)],
)
spriteset_ladle_transporter = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
)
spriteset_brick_building = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_large_shed_rear_part = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
spriteset_large_shed_front_part = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -91)],
)

sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=6,
    zoffset=68,
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_empty",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_blast_furnace_1",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_blast_furnace_1],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_blast_furnace_2",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_blast_furnace_2],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_small_shed",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_small_shed],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_brick_building",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_brick_building],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_small_tanks",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_small_tanks],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_large_shed_rear_part",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_large_shed_rear_part],
)
industry.add_spritelayout(
    id="facility_blast_furnace_spritelayout_large_shed_front_part",
    tile="wareco_base_tile_1",
    ground_sprite=spriteset_ground_tile_dark,
    ground_overlay=spriteset_ground_tile_dark,
    building_sprites=[spriteset_large_shed_front_part],
)

industry.add_industry_layout(
    id="facility_blast_furnace_industry_layout_1",
    layout=[
        (0, 0, "facility_blast_furnace_spritelayout_large_shed_rear_part"),
        (0, 1, "facility_blast_furnace_spritelayout_blast_furnace_1"),
        (1, 0, "facility_blast_furnace_spritelayout_large_shed_front_part"),
        (1, 1, "facility_blast_furnace_spritelayout_blast_furnace_2"),
        (2, 0, "facility_blast_furnace_spritelayout_small_shed"),
        (2, 1, "facility_blast_furnace_spritelayout_empty"),
    ],
)