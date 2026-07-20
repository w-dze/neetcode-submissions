import heapq;
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       #make a max heap
       #and then keep pop until that k
       max_heap = [-x for x in nums]
       heapq.heapify(max_heap) 

       count = 1
       while count < k:
            heapq.heappop(max_heap)
            count +=1

       return -max_heap[0]