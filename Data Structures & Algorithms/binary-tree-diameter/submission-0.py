# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dist2Leaves(self, root):
        if not root:
            return (0,0)
        elif (root.left==None and root.right==None):
            return (1, 0)
        else:
            ld, maxl = self.dist2Leaves(root.left)
            lr, maxr = self.dist2Leaves(root.right)
            current_dist = ld + lr
            return (1+max(ld,lr), max(maxl, maxr, current_dist))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, max_dist = self.dist2Leaves(root)
        return max_dist


        