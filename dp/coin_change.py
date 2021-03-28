def coin_change(coins, amount):
    ar = [0] + [float('inf' for i in range(amount))]
    for amt in range(1, amt+1):
        for coin in coins:
            if amt >= coin: # amount has to be greater than denomination
                # use current combo of coins or use new coin
                ar[amt] = min(ar[amt], ar[amt-coin]+1)
    return ar[-1] if ar[-1] != float('inf') else -1