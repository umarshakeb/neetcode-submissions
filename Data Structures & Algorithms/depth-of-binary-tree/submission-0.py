# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = int(self.maxDepth(root.left))
        rightDepth = int(self.maxDepth(root.right))
        max_depth = 1 + max(leftDepth,rightDepth)
        return max_depth
        