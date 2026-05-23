# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recursiveSearch(node:TreeNode) -> int:
            if not node:
                return 0
            leftS = recursiveSearch(node.left)
            rightS = recursiveSearch(node.right)
            potentialS = max(0, leftS, rightS)
            middleValue = potentialS + node.val
            headVal = max(0, leftS) + max(0, rightS) + node.val
            if headVal > self.maxPathVal:
                self.maxPathVal = headVal
            return middleValue
        
        
        #maxLR = dict()
        self.maxPathVal = -1001
        recursiveSearch(root)
        return self.maxPathVal
        
        

        