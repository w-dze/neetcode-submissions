class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        for num in nums:
            if num not in hashset:
                hashset[num] = 1
            hashset[num] +=1
        
        keys = [key for key, value in sorted(hashset.items(), key=lambda item: item[1], reverse=True)][:k]

        return keys