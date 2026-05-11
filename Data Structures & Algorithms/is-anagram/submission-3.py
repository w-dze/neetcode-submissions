class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length is not the same
        #return false immediately
        if len(s) != len(t):
            return False
            
        #dictionary
        one = {}
        two = {}

        for string in s:
            one[string] = one.get(string, 0) + 1
        
        for string in t:
            two[string] = two.get(string,0) + 1

        return one == two
 
        #time complexity: O(n)
        #space complexity: O(n)