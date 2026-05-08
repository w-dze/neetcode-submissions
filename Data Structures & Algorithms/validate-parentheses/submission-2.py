class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'}':'{', ')': '(', ']':'['}
        stack = []
        for symbol in s:
            if symbol in dictionary.values():
                stack.append(symbol)
            elif not stack:
                return False
            elif stack[-1] != dictionary[symbol]:
                return False
            else:
                stack.pop()
        
        if not stack:
            return True
        else:
            return False
        