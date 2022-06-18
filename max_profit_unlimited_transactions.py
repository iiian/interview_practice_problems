def max_profit_unlimited_transactions(prices):
    profit = 0
    for i in range(1, len(prices)):
        buy_price, sell_price = prices[i-1:i+1]
        if sell_price > buy_price:
            profit += sell_price - buy_price
    return profit