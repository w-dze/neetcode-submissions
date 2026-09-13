# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    # use dfs to traverse a tree
    # track the maximum value
    # global variable to track the "good" nodes
    # if larger, then update the max and also count as "good"
        good = 0
        stack = [(root, root.val)]

        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                good+=1

            new_max = max(max_so_far, node.val)

            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
    
        return good
