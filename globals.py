###############
### GLOBALS ###
###############

POSITION_LIMITS = {
    "BOND": 100,
    "VALE": 10,
    "VALBZ": 10,
    "GS": 100,
    "MS": 100,
    "WFC": 100,
    "XLF": 100,
}

###############
## VARIABLES ##
###############

# Our positions in each symbol
curr_positions_filled = {
    "BOND": 0,
    "VALBZ": 0,
    "VALE": 0,
    "GS": 0,
    "MS": 0,
    "WFC": 0,
    "XLF": 0,
}

# Our positions in each symbol
curr_positions_requested = {
    "BOND": 0,
    "VALBZ": 0,
    "VALE": 0,
    "GS": 0,
    "MS": 0,
    "WFC": 0,
    "XLF": 0,
}

# If a symbol is open or not
symbol_status = {
    "BOND": False,
    "VALBZ": False,
    "VALE": False,
    "GS": False,
    "MS": False,
    "WFC": False,
    "XLF": False,
}

# The trade book for all symbols
# Format is in symbol -> {buy: {}, sell: {}}
symbol_book = {
    "BOND": {},
    "VALBZ": {},
    "VALE": {},
    "GS": {},
    "MS": {},
    "WFC": {},
    "XLF": {},
}

# Tracker of all orders placed with order_id as key

orders = {}

# symbol : [all order_ids for acked orders w/ that symbol] 
ack_book = {
    "GS": [],
    "MS": [],
    "WFC": [],
    "XLF": [],
}

global_id = 0
