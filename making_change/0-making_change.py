#!/usr/bin/python3
""" Making Change module """


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    # Initialisation du DP (infiniment grand au début)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
