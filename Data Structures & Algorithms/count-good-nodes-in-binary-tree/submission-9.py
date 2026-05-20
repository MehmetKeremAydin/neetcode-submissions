# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodeSearch(self, root:TreeNode, curMax:int):
        if not root:
            return 0
        numGoodNodes = 1 if root.val >= curMax else 0
        numGoodNodesLeft = self.goodNodeSearch(root.left, max(curMax, root.val))
        numGoodNodesRight = self.goodNodeSearch(root.right, max(curMax, root.val))
        return numGoodNodes + numGoodNodesLeft + numGoodNodesRight

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodeSearch(root, -101)

        