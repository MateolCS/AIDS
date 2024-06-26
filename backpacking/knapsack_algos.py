def knapsack_dynamic(capacity, weights, values, n):
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

def knapsack_greedy(capacity, weights, values, n):
    # Calculate value-to-weight ratio
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by value-to-weight ratio in descending order
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    included_items = []
    
    for r in ratio:
        if capacity - r[1] >= 0:
            # If the entire item can be included
            capacity -= r[1]
            total_value += r[2]
            included_items.append((r[1], r[2]))  # (weight, value)
        else:
            # If only a fraction of the item can be included
            fraction = capacity / r[1]
            total_value += r[2] * fraction
            included_items.append((capacity, r[2] * fraction))  # (weight, value)
            break
    
    return total_value, included_items

def brute_force_knapsack(capacity, weights, values, n):
    def knapsack_recursive(index, remaining_capacity):
        if index == n or remaining_capacity == 0:
            return 0, []

        # Exclude the current item
        exclude_value, exclude_items = knapsack_recursive(index + 1, remaining_capacity)

        # Include the current item (if it fits)
        include_value = 0
        include_items = []
        if weights[index] <= remaining_capacity:
            include_value, include_items = knapsack_recursive(index + 1, remaining_capacity - weights[index])
            include_value += values[index]
            include_items = include_items + [(weights[index], values[index])]
        
        # Return the better of the two choices
        if include_value > exclude_value:
            return include_value, include_items
        else:
            return exclude_value, exclude_items
    
    max_value, included_items = knapsack_recursive(0, capacity)
    return max_value, included_items

