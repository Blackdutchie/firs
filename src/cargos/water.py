from cargo import Cargo

cargo = Cargo(
    id="water",
    type_name="string(STR_CARGO_NAME_WATER)",
    unit_name="string(STR_CARGO_NAME_WATER)",
    type_abbreviation="string(STR_CID_WATER)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.9",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="WATR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_WATER)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=55,
    capacity_multiplier="1",
    icon_indices=(13, 0),
    sprites_complete=True,
)
