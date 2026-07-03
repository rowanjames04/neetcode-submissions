class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to find the max positive difference between two values
        # in the price array

        l, r = 0, 1 # left = buy, right = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP