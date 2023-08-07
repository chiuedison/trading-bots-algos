from globals import *
import time

def execute_trades(exchange, trades):
    global orders
    #print("Executing trades\n\n")
    for trade in trades:
        exchange.send_add_message(trade["order_id"], trade["symbol"], trade["dir"], trade["price"], trade["size"])
        orders[trade["order_id"]] = (trade["dir"], trade["symbol"], trade["price"], trade["size"])
        time.sleep(0.1)

def update_positions_filled(message):
    global curr_positions_filled
    if message["dir"] == "SELL":
        curr_positions_filled[message["symbol"]] -= message["size"] 
    elif message["dir"] == "BUY":
        curr_positions_filled[message["symbol"]] += message["size"] 

def update_positions_requested(message):
    global curr_positions_requested
    global orders
    order = orders[message["order_id"]]
    if order["dir"] == "SELL":
        curr_positions_requested[order["symbol"]] -= order["size"] 
    elif order["dir"] == "BUY":
        curr_positions_requested[order["symbol"]] += order["size"] 

# update ack_book
def update_ack_book(message):
    global ack_book
    global orders
    order_id = message["order_id"]
    symbol = orders[order_id][1]
    #print(f"updating {symbol} in ackbook")
    ack_book[symbol].append(order_id)

def update_book(book_message):
    global symbol_book
    symbol_book[book_message["symbol"]]["buy"] = book_message["buy"]
    symbol_book[book_message["symbol"]]["sell"] = book_message["sell"]