def ways_to_make_change(coins, amount):
    ways = [0 for _ in range(amount + 1)]
    ways[0] = 1
    for coin in coins:
        for amt in range(coin, amount + 1):
            ways[amt] += ways[amt - coin]

    return ways[amount]

from testing import test_case

test_case(
    "It should return the number of ways",
    ways_to_make_change([1], 20),
    1
)
test_case(
    "It should return the number of ways",
    ways_to_make_change([1, 19], 20),
    2
)
test_case(
    "It should return the number of ways",
    ways_to_make_change([7, 4], 9),
    0
)