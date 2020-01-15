prices = [2,4,1] #[7,1,5,3,6,4] [7,6,4,3,1]

def maxProfit(prices):

    max_profit = 0
    min_price_so_far = float('inf')

    for current_price in prices:
        min_price_so_far = min(current_price, min_price_so_far)
        best_possible_profit_if_sold_now = current_price - min_price_so_far
        max_profit = max(best_possible_profit_if_sold_now, max_profit)

    return max_profit


x = maxProfit(prices)
print(x)