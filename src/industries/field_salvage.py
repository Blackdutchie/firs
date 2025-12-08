from industry import IndustryPrimaryResourceField, TileLocationChecks

industry = IndustryPrimaryResourceField(
    id="field_salvage",
    prod_cargo_types_with_multipliers=[("SALV", 20)],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="7",
    map_colour="209",
    colour_scheme_name="scheme_1_elton",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.0",
    name="string(STR_IND_FIELD_SALVAGE)",
    nearby_station_name="string(STR_STATION_COLLIERY)",
    fund_cost_multiplier="255",
    pollution_and_squalor_factor=1,
    provides_snow=False,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)
industry.enable_in_economy(
    "WAR_ECONOMY",
    prob_map_gen="9",
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)

industry.add_tile(
    id="field_salvage_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_1_bulldozer = industry.add_spriteset(
    sprites=[(10, 10, 64, 55, -31, -24)],
)
spriteset_2_trucks = industry.add_spriteset(
    sprites=[(80, 10, 64, 55, -31, -24)],
)
spriteset_3_crane = industry.add_spriteset(
    sprites=[(150, 10, 64, 55, -31, -24)],
)
spriteset_4_pilebig = industry.add_spriteset(
    sprites=[(220, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_5_pilemedium = industry.add_spriteset(
    sprites=[(290, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_6_piletiny = industry.add_spriteset(
    sprites=[(360, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_7_huts = industry.add_spriteset(
    sprites=[(430, 10, 64, 55, -31, -24)],
)
spriteset_8_pilesmall = industry.add_spriteset(
    sprites=[(500, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_9_digger = industry.add_spriteset(
    sprites=[(570, 10, 64, 55, -31, -24)],
)
spriteset_10_house = industry.add_spriteset(
    sprites=[(10, 72, 64, 64, -31, -31)],
)

industry.add_spritelayout(
    id="field_salvage_spritelayout_1",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_1_bulldozer],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_2",
    tile="field_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2_trucks],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_3",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_3_crane],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_4",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_4_pilebig],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_5",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_5_pilemedium],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_6",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_6_piletiny],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_7",
    tile="field_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7_huts],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_8",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_8_pilesmall],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_9",
    tile="field_salvage_tile_1",
    ground_sprite=None,
    ground_overlay=None,
    building_sprites=[spriteset_9_digger],
)
industry.add_spritelayout(
    id="field_salvage_spritelayout_10",
    tile="field_salvage_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_10_house],
)



industry.add_industry_layout(
    id="field_salvage_industry_layout_1",
    layout=[
        (0, 0, "field_salvage_spritelayout_8"),
        (0, 1, "field_salvage_spritelayout_6"),
        (0, 2, "field_salvage_spritelayout_3"),
        (1, 0, "field_salvage_spritelayout_5"),
        (1, 1, "field_salvage_spritelayout_4"),
        (1, 2, "field_salvage_spritelayout_6"),
        (2, 0, "field_salvage_spritelayout_10"),
        (2, 1, "field_salvage_spritelayout_5"),
        (2, 2, "field_salvage_spritelayout_8"),
        (3, 1, "field_salvage_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="field_salvage_industry_layout_2",
    layout=[
        (0, 0, "field_salvage_spritelayout_5"),
        (0, 1, "field_salvage_spritelayout_8"),
        (0, 2, "field_salvage_spritelayout_10"),
        (1, 0, "field_salvage_spritelayout_6"),
        (1, 1, "field_salvage_spritelayout_4"),
        (1, 2, "field_salvage_spritelayout_5"),
        (1, 3, "field_salvage_spritelayout_2"),
        (2, 0, "field_salvage_spritelayout_8"),
        (2, 1, "field_salvage_spritelayout_6"),
        (2, 2, "field_salvage_spritelayout_3"),
    ],
)

industry.add_industry_layout(
    id="field_salvage_industry_layout_3",
    layout=[
        (0, 0, "field_salvage_spritelayout_8"),
        (0, 1, "field_salvage_spritelayout_3"),
        (0, 2, "field_salvage_spritelayout_10"),
        (1, 0, "field_salvage_spritelayout_6"),
        (1, 1, "field_salvage_spritelayout_4"),
        (1, 2, "field_salvage_spritelayout_8"),
        (2, 0, "field_salvage_spritelayout_6"),
        (2, 1, "field_salvage_spritelayout_5"),
        (2, 2, "field_salvage_spritelayout_5"),
        (2, 3, "field_salvage_spritelayout_2"),
    ],
)