import sys
import os
import json
import time
import multiprocessing
from globals import (global_id, curr_positions_requested, symbol_status, curr_positions_filled)
from main import *

def push_buys(orders_to_place, buy_book):
    global global_id
    # loop through the buy book
    for order in buy_book:
        # if the order price is over 1000, we should sell to them
        if (order[0] > 1000  and curr_positions_filled["BOND"] > -100):
            # add the order
            order_obj = {"type": "add", 
                        "order_id": global_id, 
                        "symbol": "BOND", 
                        "dir": "SELL", 
                        "price": order[0], 
                        "size": order[1]
                        }
            print(order_obj)
            # increment order_id
            global_id += 1
            # update our requested position size
            curr_positions_requested["BOND"] += order[1]
            orders_to_place.append(order_obj)
        else:
            # break the for loop if someone offers 1000 or less
            break

def push_sells(orders_to_place, sell_book):
    global global_id
    # loop through the sell book
    for order in sell_book:
        # if the order price is under 1000, we should buy from them
        if (order[0] < 1000 and curr_positions_filled["BOND"] < 100):
            # add the order
            order_obj = {"type": "add", 
                        "order_id": global_id, 
                        "symbol": "BOND", 
                        "dir": "BUY", 
                        "price": order[0], 
                        "size": order[1]
                        }
            # print(order_obj)
            # increment order_id
            global_id += 1
            # update our requested position size
            curr_positions_requested["BOND"] -= order[1]
            orders_to_place.append(order_obj)
        else:
            # break the for loop if someone offers 1000 or less
            break

# returns an array of orders we want to place
def run_bond_agent(message):
    global global_id
    orders_to_place = []
    manager = multiprocessing.Manager()
    parallel_orders = manager.list()

    # make sure the bond market is open
    if (symbol_status["BOND"] == True):
        buy_book = message["buy"]
        sell_book = message["sell"]
        process1 = multiprocessing.Process(target=push_buys, args=[parallel_orders, buy_book])
        process2 = multiprocessing.Process(target=push_sells, args=[parallel_orders, sell_book])
        process1.start()
        process2.start()
        process1.join()
        process2.join()
        # done looping through buy_books and sell_books
        return orders_to_place
    # end if
    return []

def run_bad_bond_agent():
    print("running bad bond agent")