# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #counter variable cnt to track position of current node
        #cnt == k, store the current node's value in global variable and return 
        #in order traversal 

        cnt = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            cnt += 1
        
            if cnt == k:
                return curr.val

            curr = curr.right