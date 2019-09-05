def get_max_profit(stock_prices):

    # Calculate the max profit
    
    # need to make sure you buy BEFORE you selL!! obviously!!!! so you need to cut off where 
    # in the list you bought the stock!! at what time and only sell after that~
    
    # you will never buy the stock in the last place because you will always need one free to
    # sell afterwards
    if len(stock_prices) > 1:
        buy = min(stock_prices[:len(stock_prices)-1])
        min_index = stock_prices.index(min(stock_prices[:len(stock_prices)-1]))
        max_list = stock_prices[min_index:]
        sell = max(max_list)
        ret = sell - buy
        return ret
    else:
        raise(Exception)
