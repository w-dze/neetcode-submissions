class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        length = len1-1
        
        count1 = {}
        for letter in s1:
            count1[letter] = 1+count1.get(letter,0)


        left = 0
        right = left + len1
        while right <= len(s2):
            count = {}
            for letter in s2[left:right]:
                count[letter] = 1+count.get(letter,0)
            if count == count1:
                return True
            else:
                left +=1
                right +=1

        return False            
