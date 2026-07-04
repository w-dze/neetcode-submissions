class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()

        def findSum(n):
            sum = 0
            while n > 0:
                sum += ((n%10) ** 2)
                n = n//10
            return sum

        while n != 1:
            if n in hash_set:
                return False
            hash_set.add(n)
            n = findSum(n)
        return True
            