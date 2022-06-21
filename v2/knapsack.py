def knapsack(items, max_weight):
    W = max_weight + 1
    I = len(items) + 1
    matrix = [ [
        0 for w in range(W)
    ] for i in range(I) ]

    for i in range(1, I):
        value, wt = items[i-1]
        for w in range(wt, W):
            matrix[i][w] = value + matrix[i-1][w-wt]

    return matrix[I-1][W-1]

if __name__ == "__main__":
    from testing import test_case

    test_case(
        "(1) it should return the max value collectible given the provided weight budget",
        knapsack([], 0),
        0
    )
    test_case(
        "(1) it should return the max value collectible given the provided weight budget",
        knapsack([(10, 1)], 0),
        0
    )
    test_case(
        "(1) it should return the max value collectible given the provided weight budget",
        knapsack([(10, 1)], 1),
        10
    )
    test_case(
        "(1) it should return the max value collectible given the provided weight budget",
        knapsack([(10, 1),(20,1)], 2),
        30
    )