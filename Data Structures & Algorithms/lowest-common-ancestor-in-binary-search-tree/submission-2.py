# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val <= large and root.val >= small:
                return root
            elif root.val > large:
                root = root.left
            else:
                root = root.right

        