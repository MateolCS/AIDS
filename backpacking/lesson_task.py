def knapsack(capacity, weights, values, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    included_items = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            included_items.append(i-1)
            w -= weights[i-1]

    included_items.reverse()
    
    return dp[n][capacity], included_items


capacity = 8


weights = [3, 3, 1, 4, 2, 5]
values = [3, 4, 2, 4, 3, 5]

value, elements = knapsack(capacity, weights, values, len(weights))

print(f"Maksymalna wartość {value}")
print(f"Co w plecaku {elements}")
