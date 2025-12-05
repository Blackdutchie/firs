from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="seaport",
    accept_cargos_with_input_ratios=[
        ("VEHI", 1),
        ("ITEM", 4),
        ("SHIP", 1),
        ("ARTY", 1),
        ("AVEH", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FRNT", 8),
    ],
    prob_in_game="0",
    prob_map_gen="4",
    # map_colour="186", # former orange before v5?
    # map_colour="177",  # former Bulk Terminal colour?
    map_colour="45",
    colour_scheme_name="scheme_9_shania",
    #special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    name="string(STR_IND_SEAPORT)",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_2)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)


spriteset_ground = industry.add_spriteset(
    type="pavement",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="seaport_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="seaport_industry_layout",
    layout=[(0, 0, "seaport_spritelayout")],
)
