# Qsn 1(b)
def min_time_to_build_engines(engines, split_cost):
    # Sort engines in ascending order
    engines.sort()

    max_engines = len(engines)
    dp = [float('inf') - split_cost] * (max_engines + 1)  # Dynamic programming array

    # Base case: building one engine takes its own time
    dp[1] = engines[0]

    # Iterate through each engine
    for i in range(2, max_engines + 1):
        # Iterate from current number of engineers down to 1 (representing splitting)
        for j in range(i, 0, -1):
            time = max(dp[j], engines[i - 1])  # Time to build current engine

            # If more than 1 engineer, consider splitting cost
            if j > 1:
                time = min(time, dp[j // 2] + split_cost)

            # Update minimum time for the current number of engineers
            dp[i] = min(dp[i], time)

    return dp[max_engines]  # Return minimum time for building all engines


if __name__ == "__main__":
    engines = [3, 4, 5, 2]
    split_cost = 2

    min_time = min_time_to_build_engines(engines, split_cost)
    print("Minimum time needed to build all engines:", min_time)
