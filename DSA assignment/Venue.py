def minCost(costs):
    if not costs or len(costs) == 0:
        return 0

    n = len(costs)
    k = len(costs[0])

    memo = {}

    def calculate_min_cost(i, prev_theme):
        if i == n:
            return 0

        if (i, prev_theme) in memo:
            return memo[(i, prev_theme)]

        min_cost = float('inf')
        for j in range(k):
            if j != prev_theme:
                current_cost = costs[i][j] + calculate_min_cost(i + 1, j)
                min_cost = min(min_cost, current_cost)

        memo[(i, prev_theme)] = min_cost
        return min_cost

    min_total_cost = float('inf')
    for j in range(k):
        min_total_cost = min(min_total_cost, calculate_min_cost(0, j))

    return min_total_cost


if __name__ == "__main__":
    costs = [[1, 3, 2], [4, 6, 8], [3, 1, 5]]
    minCost = minCost(costs)
    print("Minimum cost:", minCost)
