# 5) Branch & Bound - 0/1 Knapsack Problem
def knapsack_branch_bound(weights, values, capacity):
    n = len(weights)
    max_value = 0

    def backtrack(i, curr_weight, curr_value):
        nonlocal max_value
        if i == n:
            max_value = max(max_value, curr_value)
            return
        if curr_weight + weights[i] <= capacity:
            backtrack(i + 1, curr_weight + weights[i], curr_value + values[i])
        backtrack(i + 1, curr_weight, curr_value)

    backtrack(0, 0, 0)
    return max_value

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Knapsack max value:", knapsack_branch_bound(weights, values, capacity))
