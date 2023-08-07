from globals import *
from helpers import *
import time 

def run_penny_agent(exchange):
    # clear all acked orders
    global ack_book
    symbols = ["MS", "GS", "WFC", "XLF"]
    #print("Clearning ack orders...")
    # print(f"Ack book: {ack_book}")
    for symbol in symbols:
        acked_orders = ack_book[symbol]
        for order_id in acked_orders:
            # cancel that order
            exchange.send_cancel_message(order_id)
            ack_book[symbol] = []
            time.sleep(0.1)
    # done cancelling acked orders

    global global_id
    orders_to_place = []
    # go through books 
    for symbol in symbols:
        # make sure that market is open
        if symbol_status[symbol] == True:
            try:
                # print(f"Trying {symbol}")
                message = symbol_book[symbol]
                buy_book = message["buy"]
                sell_book = message["sell"]
                best_bid = buy_book[0][0]
                best_ask = sell_book[0][0]
                if (best_bid + 2) < (best_ask - 2):
                # if we are not maxed out on buys 
                    if (curr_positions_filled[symbol] < 60):
                        # beat best bid
                        # print("Appending BUY order")
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "BUY", 
                            "price": best_bid + 2, 
                            "size": 2,
                        })
                        global_id += 1
                        best_bid = best_bid + 2
                        # add levels 
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "BUY", 
                            "price": best_bid - 10, 
                            "size": 4,
                        })
                        global_id += 1
                        best_bid = best_bid + 2
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "BUY", 
                            "price": best_bid - 15, 
                            "size": 2,
                        })
                        global_id += 1
                        best_bid = best_bid + 2
            
                if (best_ask - 2) > best_bid:
                    # if we are not maxed out on sells
                    if (curr_positions_filled[symbol] > -60):
                        # beat best ask
                        # print("Appending SELL order")
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "SELL", 
                            "price": best_ask - 2, 
                            "size": 2,
                        })
                        global_id += 1
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "SELL", 
                            "price": best_ask + 10, 
                            "size": 4,
                        })
                        global_id += 1
                        orders_to_place.append({
                            "type": "add", 
                            "order_id": global_id, 
                            "symbol": symbol, 
                            "dir": "SELL", 
                            "price": best_ask + 15, 
                            "size": 2,
                        })
                        global_id += 1
            except:
                continue

    return orders_to_place 
        
