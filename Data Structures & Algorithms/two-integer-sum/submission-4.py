class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remain = target - nums[i]
            left = nums[:i] + nums[i+1:]
            if remain in left:
                second_index = nums[i+1:].index(remain)+i+1
                return [i, second_index]