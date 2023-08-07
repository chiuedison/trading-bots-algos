from globals import *
import time

def run_penny_agent(exchange, message):
    #print("new book!")
    global curr_positions_filled
    global curr_positions_requested
    global global_id
    ticker = message["symbol"]

    buy_book = message["buy"]
    sell_book = message["sell"]
    orders_to_place = []
    # we should be able to trade the symbol
    if symbol_status[ticker] == True:
        if buy_book and sell_book:
            best_bid = buy_book[0][0]
            best_ask = sell_book[0][0]
            if (best_bid + 2) < (best_ask - 2):
                # if we are not maxed out on buys 
                print(f"CURR POSITIONS FILLED FOR TICKER {ticker}\n", curr_positions_filled[ticker])
                if (curr_positions_filled[ticker] < 100):
                    # beat best bid
                    orders_to_place.append({
                        "type": "add", 
                        "order_id": global_id, 
                        "symbol": ticker, 
                        "dir": "BUY", 
                        "price": best_bid + 2, 
                        "size": 40 - curr_positions_filled[ticker],
                    })
                    global_id += 1
                    best_bid = best_bid + 2
            
            if (best_ask - 2) > best_bid:
                # if we are not maxed out on sells
                if (curr_positions_filled[ticker] > -100):
                    # beat best ask
                    orders_to_place.append({
                        "type": "add", 
                        "order_id": global_id, 
                        "symbol": ticker, 
                        "dir": "SELL", 
                        "price": best_ask - 2, 
                        "size": 40 + curr_positions_filled[ticker],
                    })
                    global_id += 1

    return orders_to_place 
        
