import sys
import os
import json
import time
import multiprocessing
from globals import *
# 10 XLF = 3 BOND + 2 GS + 3 MS + 2 WFC


# function that looks at book and decides if it is safe to convert to etf or stocks
# modifies conversion_type to "to_etf" or "to_stocks" if valid conversion is found
# returns bool
def should_convert(conversion_type) -> bool:
    global symbol_book
    if symbol_book["BOND"] and symbol_book["BOND"]["buy"] and symbol_book["BOND"]["sell"]:
        BOND_best_bid = symbol_book["BOND"]["buy"][0][0]
        BOND_best_ask = symbol_book["BOND"]["sell"][0][0]
    else:
        return False
    if symbol_book["GS"] and symbol_book["GS"]["buy"] and symbol_book["GS"]["sell"]:    
        GS_best_bid = symbol_book["GS"]["buy"][0][0]
        GS_best_ask = symbol_book["GS"]["sell"][0][0]
    else:
        return False
    if symbol_book["MS"] and symbol_book["MS"]["buy"] and symbol_book["MS"]["sell"]:
        MS_best_bid = symbol_book["MS"]["buy"][0][0]
        MS_best_ask = symbol_book["MS"]["sell"][0][0]
    else:
        return False
    if symbol_book["WFC"] and symbol_book["WFC"]["buy"] and symbol_book["WFC"]["sell"]:
        WFC_best_bid = symbol_book["WFC"]["buy"][0][0]
        WFC_best_ask = symbol_book["WFC"]["sell"][0][0]
    else:
        return False
    
    bid_value_of_symbols = (3*BOND_best_bid) + (2*GS_best_bid) + (3*MS_best_bid) + (2*WFC_best_bid)
    ask_value_of_symbols = (3*BOND_best_ask) + (2*GS_best_ask) + (3*MS_best_ask) + (2*WFC_best_ask)

    if symbol_book["XLF"] and symbol_book["XLF"]["buy"] and symbol_book["XLF"]["sell"]:
        bid_value_of_etf = symbol_book["XLF"]["buy"][0][0]*10
        ask_value_of_etf = symbol_book["XLF"]["sell"][0][0]*10
    else:
        return False

    #print(bid_value_of_symbols)
    #print(ask_value_of_etf)
    if (bid_value_of_symbols + 1) < ask_value_of_etf:
        conversion_type = "to_etf"
    elif (ask_value_of_symbols - 1) > bid_value_of_etf:
        conversion_type = "to_stocks"
    else:
        conversion_type = ""
    return True

def update_book(book_message):
    global symbol_book
    symbol_book[book_message["symbol"]]["buy"] = book_message["buy"]
    symbol_book[book_message["symbol"]]["sell"] = book_message["sell"]

def run_conversion_agent(exchange):
    global order_id
    conversion_type = "a"
    if (should_convert(conversion_type)):
        # do the conversion
        print(f"Converting to {conversion_type}")
        if conversion_type == "to_etf":
            # convert stocks to etf
            # buy stocks
            best_bond_book_buy = symbol_book["BOND"]["buy"][0][0]
            exchange.send_add_messsage(order_id, "BOND", "BUY", best_bond_book_buy + 1, 3)
            order_id += 1
            time.sleep(0.1)

            best_gs_book_buy = symbol_book["GS"]["buy"][0][0]
            exchange.send_add_messsage(order_id, "GS", "BUY", best_gs_book_buy + 1, 2)
            order_id += 1
            time.sleep(0.1)
            
            best_ms_book_buy = symbol_book["MS"]["buy"][0][0]
            exchange.send_add_messsage(order_id, "MS", "BUY", best_ms_book_buy + 1, 3)
            order_id += 1
            time.sleep(0.1)

            best_wfc_book_buy = symbol_book["WFC"]["buy"][0][0]
            exchange.send_add_messsage(order_id, "WFC", "BUY", best_wfc_book_buy + 1, 2)
            order_id += 1
            time.sleep(0.1)
            
            # convert
            time.sleep(0.1)
            # exchange.send_convert_message(order_id, "XLF", "BUY", 10)
            
            # sell ETF
            ask_value_of_etf = symbol_book["XLF"]["sell"][0][0]
            exchange.send_add_messsage(order_id, "XLF", "SELL", ask_value_of_etf - 1, 10)
            
        if conversion_type == "to_stocks":
            # convert etf to stocks
            # buy 10 etfs
            
            pass
        pass
        


