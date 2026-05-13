class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        for num in nums:
            hashset[num] = hashset.get(num,0) + 1
        
        heap = []
        for num in hashset.keys():
            heapq.heappush(heap,(hashset[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res