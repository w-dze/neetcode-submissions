class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        # sum is too big, right pointer move left
        # sum is too small, left pointer move right
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left +=1
        return [left+1, right+1]