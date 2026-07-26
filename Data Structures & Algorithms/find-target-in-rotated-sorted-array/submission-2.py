class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # there is a deflection point
        # there could be pointers l , r , and mid

        # if l and mid are in the same segment, nums[l] < nums[mid]
        # so the pivot is in the right part

        # if r and mid are in the same segment, nums[mid] < nums[r]
        # the pivot is in the left part

        # once we find the pivot, 
        # we can do binary search on the corresponding segment

        l , r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            #right sorted portion
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


        
            
            