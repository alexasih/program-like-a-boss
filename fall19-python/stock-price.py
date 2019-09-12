def get_max_profit(stock_prices):

    # Calculate the max profit
    
    if len(stock_prices) < 2:
        raise(Exception)
    
    
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    print(min_price)
    
    for val in stock_prices[1:]:
        profit = val - min_price
        max_profit = max(profit, max_profit)
        min_price = min(val, min_price)
        print(min_price)

    return max_profit
