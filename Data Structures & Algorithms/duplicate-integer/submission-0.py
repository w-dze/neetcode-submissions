class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for num in nums:
            if num not in arr:
                arr.append(num)
            else:
                return True
        return False