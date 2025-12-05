from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="bunker_base",
    accept_cargo_types=["FRNT"],
    prod_cargo_types=[],
    prob_in_game="18",
    prob_map_gen="24",
    prod_multiplier="[0, 0]",
    map_colour="169",
    colour_scheme_name="scheme_3_hendrix",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_BUNKER_BASE)",
    nearby_station_name="string(STR_STATION_TOWN_1)",
    fund_cost_multiplier="15",
    provides_snow=True,
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
    id="bunker_base_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="bunker_base_industry_layout",
    layout=[(0, 0, "storage_depot_spritelayout")],
)
