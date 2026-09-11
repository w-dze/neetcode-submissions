# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # so we still do a traversal of the entire tree
        # and then the last node in each level 
        # BFS
        if not root:
            return []

        result = []
        
        queue = deque([root])

        while queue:
            level_length = len(queue)

            i = 1
            while i < level_length:
                node = queue.popleft()
                i+=1
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            last_node = queue.popleft()
            result.append(last_node.val)

            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)
        
        return result
            
            
