class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if n - 1 is not in nums
        #then it could be a possible start
        numset = set(nums)
        longest = 0
        for num in numset:
            if num - 1 not in numset:
                curr = num
                length = 1

                while curr + 1 in numset:
                    curr +=1
                    length +=1
                longest = max(longest,length)
        return longest
