class Solution:
    def climbStairs(self, n: int) -> int:
        #create a n-sized array cache 
        #if cache[i] already exists, return that value
        #else
        #the minimum return value between the two is the result

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one