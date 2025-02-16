# 3) Greedy Algorithm - Coin Change Problem
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count

print("Coins needed for 63:", min_coins([1, 5, 10, 25], 63))
