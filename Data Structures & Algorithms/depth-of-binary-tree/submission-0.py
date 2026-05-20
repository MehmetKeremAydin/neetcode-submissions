# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dist2bottom(self, root:TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.dist2bottom(root.left), self.dist2bottom(root.right))
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dist2bottom(root)
        
        