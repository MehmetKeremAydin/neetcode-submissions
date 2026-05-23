# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recursiveSearch(node:TreeNode, maxPathVal) -> tuple(int, int):
            if not node:
                return 0, maxPathVal
            leftS, maxPathVal = recursiveSearch(node.left, maxPathVal)
            rightS, maxPathVal = recursiveSearch(node.right, maxPathVal)
            potentialS = max(0, leftS, rightS)
            middleValue = potentialS + node.val
            headVal = max(0, leftS) + max(0, rightS) + node.val
            if headVal > maxPathVal:
                maxPathVal = headVal
            return middleValue, maxPathVal 
        #maxLR = dict()
        maxPathVal = -1001
        _, maxPathVal = recursiveSearch(root, maxPathVal)
        return maxPathVal
        
        

        