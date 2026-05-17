class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(numbers):
            remain = target - num
            if remain in dictionary.keys():
                return [dictionary[remain]+1, index+1]
            dictionary[num] = index