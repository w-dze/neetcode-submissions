class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if i is the sell value
        #i have to choose the minimum from the left of i
        i = 1
        maximum = 0
        while i < len(prices):
            minimum = min(prices[:i])
            curr = prices[i] - minimum
            maximum = max(maximum, curr)
            i+=1
        return maximum