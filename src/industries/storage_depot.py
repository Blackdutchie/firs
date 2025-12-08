from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="storage_depot",
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
    prob_map_gen="10",
    map_colour="207",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(
        same_type_distance=32,
    ),
    special_flags=["IND_FLAG_BUILT_NEAR_TOWN"],
    name="string(STR_IND_STORAGE_DEPOT)",
    nearby_station_name="string(STR_STATION_VEHICLE_DISTRIBUTOR)",
    fund_cost_multiplier="255",
    provides_snow=False,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

industry.add_tile(
    id="storage_depot_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="storage_depot_tile_2",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True, require_road_adjacent=True
    ),
)
spriteset_ground = industry.add_spriteset(
    type="pavement",
)

spriteset_crane_rails_nw_se = industry.add_spriteset(
    sprites=[(181, 505, 64, 39, -31, -1)],
    always_draw=True,
)
spriteset_crane_rails_ne_sw = industry.add_spriteset(
    sprites=[(251, 505, 64, 39, -31, -1)],
    always_draw=True,
)
spriteset_warehouse_full_nw_se = industry.add_spriteset(
    sprites=[(720, 10, 64, 84, -31, -51)],
)
spriteset_warehouse_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 10, 64, 84, -31, -51)],
)

spriteset_large_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 410, 64, 84, -34, -53)],
    always_draw=True,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 410, 64, 84, -34, -53)],
    always_draw=True,
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_empty",
    ground_sprite=spriteset_ground,
    tile="storage_depot_tile_1",
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_crane_rails_nw_se",
    ground_sprite=spriteset_ground,
    tile="storage_depot_tile_2",
    ground_overlay=None,
    building_sprites=[spriteset_crane_rails_nw_se],
    fences=["sw"],
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_crane_rails_ne_sw",
    tile="storage_depot_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_crane_rails_ne_sw],
    fences=["nw"],
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_warehouse_full_nw_se",
    tile="storage_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_warehouse_full_nw_se],
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_warehouse_full_ne_sw",
    ground_sprite=spriteset_ground,
    tile="storage_depot_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_warehouse_full_ne_sw],
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_large_crane_ne_sw",
    ground_sprite=spriteset_ground,
    tile="storage_depot_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_large_crane_ne_sw],
    fences=["sw"],
)
industry.add_spritelayout(
    id="storage_depot_spritelayout_spriteset_large_crane_nw_se",
    ground_sprite=spriteset_ground,
    tile="storage_depot_tile_1",
    ground_overlay=None,
    building_sprites=[spriteset_large_crane_nw_se],
    fences=["nw"],
)
industry.add_industry_layout(
    id="storage_depot_industry_layout_1",
    layout=[
        (0, 0, "storage_depot_spritelayout_spriteset_warehouse_full_nw_se"),
        (0, 1, "storage_depot_spritelayout_spriteset_warehouse_full_nw_se"),
        (1, 0, "storage_depot_spritelayout_spriteset_large_crane_ne_sw"),
        (1, 1, "storage_depot_spritelayout_spriteset_crane_rails_nw_se"),
    ],
)

industry.add_industry_layout(
    id="storage_depot_industry_layout_3",
    layout=[
        (0, 0, "storage_depot_spritelayout_spriteset_large_crane_nw_se"),
        (0, 1, "storage_depot_spritelayout_spriteset_warehouse_full_ne_sw"),
        (1, 0, "storage_depot_spritelayout_spriteset_crane_rails_ne_sw"),
        (1, 1, "storage_depot_spritelayout_spriteset_warehouse_full_ne_sw"),
    ],
)