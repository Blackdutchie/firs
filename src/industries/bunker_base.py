from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="bunker_base",
    accept_cargo_types=["FRNT"],
    prod_cargo_types=[],
    prob_in_game="0",
    prob_map_gen="1",
    prod_multiplier="[0, 0]",
    map_colour="169",
    colour_scheme_name="scheme_3_hendrix",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_BUNKER_BASE)",
    nearby_station_name="string(STR_STATION_TOWN_1)",
    fund_cost_multiplier="3",
    provides_snow=False,
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
    id="bunker_base_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
spriteset_1 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)

spriteset_2 = industry.add_spriteset(
    sprites=[(220, 10, 64, 92, -31, -60)],
)

industry.add_spritelayout(
    id="bunker_base_spritelayout_1",
    tile="bunker_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="bunker_base_spritelayout_2",
    tile="bunker_base_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
)
industry.add_industry_layout(
    id="bunker_base_industry_layout_1",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_2"),
        (1, 1, "bunker_base_spritelayout_1"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="bunker_base_industry_layout_2",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_2"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="bunker_base_industry_layout_3",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_2"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_1"),
        (1, 2, "bunker_base_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="bunker_base_industry_layout_4",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_2"),
        (1, 2, "bunker_base_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="bunker_base_industry_layout_5",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_2"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_1"),
        (1, 2, "bunker_base_spritelayout_1"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_1"),
        (2, 2, "bunker_base_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="bunker_base_industry_layout_6",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_2"),
        (1, 1, "bunker_base_spritelayout_1"),
        (1, 2, "bunker_base_spritelayout_1"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_1"),
        (2, 2, "bunker_base_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="bunker_base_industry_layout_7",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_1"),
        (1, 2, "bunker_base_spritelayout_2"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_1"),
        (2, 2, "bunker_base_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="bunker_base_industry_layout_8",
    layout=[
        (0, 0, "bunker_base_spritelayout_1"),
        (0, 1, "bunker_base_spritelayout_1"),
        (0, 2, "bunker_base_spritelayout_1"),
        (1, 0, "bunker_base_spritelayout_1"),
        (1, 1, "bunker_base_spritelayout_1"),
        (1, 2, "bunker_base_spritelayout_1"),
        (2, 0, "bunker_base_spritelayout_1"),
        (2, 1, "bunker_base_spritelayout_2"),
        (2, 2, "bunker_base_spritelayout_1"),
    ],
)