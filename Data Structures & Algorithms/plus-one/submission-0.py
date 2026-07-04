class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if the last digit is not 9, I can just add 1 and return
        # if it is 9, then I would turn it to 0, and then carry the 1 over
        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0 
        return [1] + digits