class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        # sum is too big, right pointer move left
        # sum is too small, left pointer move right
        left = 0
        right = len(numbers) - 1
        while left < right: 
            curr = numbers[left] + numbers[right]
            if curr > target:
                right -=1
            elif curr < target:
                left +=1
            else:
                return [left+1, right+1]