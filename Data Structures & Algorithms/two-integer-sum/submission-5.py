class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, n in enumerate(nums):
            remain = target - n
            if remain in dictionary:
                return [dictionary[remain],i]
            dictionary[n] = i