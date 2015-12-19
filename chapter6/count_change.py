def count_change(n, coins):
    if n == 0:
        return 1
    elif n < 0 or len(coins) == 0:
        return 0
    return count_change(n, coins[1:]) + count_change(n - coins[0], coins)
print count_change(10, [1,2])
