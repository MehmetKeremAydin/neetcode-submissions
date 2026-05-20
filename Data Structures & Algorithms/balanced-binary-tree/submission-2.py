# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBalance(self, root: TreeNode) -> (bool, int):
        if not root:
            return (True, 0)
        balL, heightL = self.checkBalance(root.left)
        balR, heightR = self.checkBalance(root.right)
        balC = abs(heightL - heightR) < 2
        return (balL and balR and balC, 1+max(heightL,heightR))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, h = self.checkBalance(root)
        print(h)
        return balanced
        