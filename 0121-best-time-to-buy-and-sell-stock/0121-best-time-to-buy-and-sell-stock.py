class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - lowest_price)
        return max_profit

