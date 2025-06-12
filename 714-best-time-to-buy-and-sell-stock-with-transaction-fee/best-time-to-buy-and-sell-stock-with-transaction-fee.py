class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        profit_no_stock = 0
        profit_with_stock = -prices[0]

        for price in prices[1:]:
            profit_no_stock = max(profit_no_stock, profit_with_stock + price - fee)
            profit_with_stock = max(profit_with_stock, profit_no_stock - price)

        return profit_no_stock