class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer
        #(j - i) * min(height[j], height[i])
        #and move pointer for whichever one is smaller
        i, j = 0, len(heights)-1
        maximum = 0
        while i < j:
            curr = (j-i)*min(heights[i], heights[j])
            if curr > maximum:
                maximum = curr
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maximum