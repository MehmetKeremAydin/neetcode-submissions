# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def DFS(node:TreeNode, canRob:bool) -> int:
            if (node, canRob) in memory:
                return memory[(node, canRob)]
            if node == None:
                return 0
            if canRob:
                # We rob this node:
                robbed = DFS(node.left, False) + DFS(node.right, False) + node.val
                # We skip robbing this node:
                skipped = DFS(node.left, True) + DFS(node.right, True)
            else:
                robbed = 0 # We can not rob. 
                skipped = DFS(node.left, True) + DFS(node.right, True)
            maxProfit = max(robbed, skipped)
            memory[(node, canRob)] = maxProfit
            return maxProfit
        memory = {}
        return DFS(root, True)