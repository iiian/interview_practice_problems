def max_profit_k_transactions(prices, k):
    max_profit_matrix = [
        [0 for _ in range(k + 1)] 
        for _ in range(len(prices))
    ]
    
    for sell_day in range(1, len(prices)):
        for tx_no in range(1,k+1):
            profit = 0
            for buy_day in range(sell_day):
                profit = max(
                    profit,
                    prices[sell_day] - prices[buy_day] + max_profit_matrix[buy_day][tx_no-1]    
                )
            
            max_profit_matrix[sell_day][tx_no] = max(
                profit,
                max_profit_matrix[sell_day-1][tx_no]
            )   

    return max_profit_matrix[len(prices)-1][k]

if __name__ == "__main__":
    from testing import test_case

    test_case(
        "it should return the max profit given the allocated number of transactions",
        max_profit_k_transactions([10,20,19,15,25,20,3,13,6,9,4,7], 3),
        30
    )

    for i in range(20):
        max_profit_k_transactions([20, 20, 19, 20, 23, 23, 24, 26, 29, 29, 29 ,29, 28, 25, 20, 12, 12,12,12,12,12,12,13,14,15,16,16,16,16,17,18,19,19,19,20,22,24,26,26,26,26,28,28,30,33,36,40,44,50,60,80,80,80,80,80,80,85,75,72,70,70,70,70,70,69,69,70,69,30,69,70,71,73,78,79,80,81,81,82,82,82,83,86,88,90,100,100,100,100,100,99], i),
        