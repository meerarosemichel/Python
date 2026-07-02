class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
            
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)
