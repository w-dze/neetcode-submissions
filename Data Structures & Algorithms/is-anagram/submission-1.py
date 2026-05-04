class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #start with one string
        #go through every letter in the first string
        #and then go find that same letter in the second string
        #pop the letter from the word if i found
        #return true if the second string is empty

        #if they are not the same length then they for sure cannot be the annagrams
        if len(s) != len(t):
            return False
        for string in s:
            if string in t:
                index = t.index(string)
                if index != -1:
                    t = t[:index] + t[index+1:]
                else:
                    return False
            else:
                return False
            
        if t == "":
            return True
        else:
            return False