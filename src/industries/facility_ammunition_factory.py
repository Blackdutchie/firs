from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="facility_ammunition_factory",
    accept_cargos_with_input_ratios=[
        ("HEPW", 4),
        ("CMAT", 4),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ARTY", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="0",
    map_colour="10",
    colour_scheme_name="scheme_2_dylan", # cabbage needs checked
    name="string(STR_IND_FACILITY_AMMUNITION_FACTORY)",
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
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)

industry.add_tile(
    id="facility_ammunition_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_crane_SE = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -50)],
)

spriteset_shed = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -50)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -50)],
)


industry.add_spritelayout(
    id="facility_ammunition_factory_spritelayout_empty",
    tile="facility_ammunition_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)
industry.add_spritelayout(
    id="facility_ammunition_factory_spritelayout_1",
    tile="facility_ammunition_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crane_SE],
)
industry.add_spritelayout(
    id="facility_ammunition_factory_spritelayout_2",
    tile="facility_ammunition_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_shed],
)
industry.add_spritelayout(
    id="facility_ammunition_factory_spritelayout_3",
    tile="facility_ammunition_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tanks],
)
industry.add_industry_layout(
    id="facility_ammunition_factory_industry_layout_1",
    layout=[
        (0, 0, "facility_ammunition_factory_spritelayout_2"),
        (0, 1, "facility_ammunition_factory_spritelayout_3"),
        (1, 0, "facility_ammunition_factory_spritelayout_2"),
        (1, 1, "facility_ammunition_factory_spritelayout_1"),
        (2, 0, "facility_ammunition_factory_spritelayout_2"),
        (2, 1, "facility_ammunition_factory_spritelayout_empty"),
    ],
)