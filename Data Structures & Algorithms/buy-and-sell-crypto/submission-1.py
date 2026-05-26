class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if i is the sell value
        #i have to choose the minimum from the left of i
        maximum = 0
        minimum = prices[0]
        for price in prices:
            minimum = min(minimum,price)
            curr = price - minimum
            maximum = max(maximum, curr)
        return maximum