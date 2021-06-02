# must buy before sell
# keep track of min price, max price
# max price must come after min price
# no need to keep tracker of max price


def maxProfit(prices):
    if not prices:
        return 0
    imin = prices[0]
    max_prof = 0
    for i in range(1, len(prices)):
        if prices[i]-imin > max_prof:
            max_prof = prices[i]-imin
        elif prices[i] < imin:
            imin = prices[i]
    return max_prof
