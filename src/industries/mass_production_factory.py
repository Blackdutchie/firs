from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="mass_production_factory",
    accept_cargos_with_input_ratios=[
        ("BMAT", 6),
        ("RMAT", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ITEM", 6),
        ("SHIP", 2),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE",
    prob_in_game="0",
    prob_map_gen="10",
    map_colour="157",
    colour_scheme_name="scheme_12_mariah", # cabbage needs checked
    name="string(STR_IND_MASS_PRODUCTION_FACTORY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="255",
    special_flags=["IND_FLAG_BUILT_NEAR_TOWN"],
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

industry.add_tile(
    id="mass_production_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -23)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(10, 146, 64, 31, -31, 0)],
)

spriteset_8 = industry.add_spriteset(
    sprites=[(80, 146, 64, 84, -31, -54)],
)

spriteset_9 = industry.add_spriteset(
    sprites=[(150, 146, 64, 84, -31, -54)],
)



sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id="mass_production_factory_spritelayout_1",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_2",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_3",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_4",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_5",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_6",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_empty",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_7",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_8",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="mass_production_factory_spritelayout_9",
    tile="mass_production_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="mass_production_factory_industry_layout_1",
    layout=[

        (0, 0, "mass_production_factory_spritelayout_empty"),
        (0, 1, "mass_production_factory_spritelayout_7"),
        (0, 2, "mass_production_factory_spritelayout_3"),
        (0, 3, "mass_production_factory_spritelayout_3"),
        (0, 4, "mass_production_factory_spritelayout_4"),
        (1, 0, "mass_production_factory_spritelayout_8"),
        (1, 1, "mass_production_factory_spritelayout_7"),
        (1, 2, "mass_production_factory_spritelayout_3"),
        (1, 3, "mass_production_factory_spritelayout_3"),
        (1, 4, "mass_production_factory_spritelayout_9"),
    ],
)
