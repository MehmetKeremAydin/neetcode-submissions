# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root:TreeNode, minVal:int, maxVal:int):
            if not root:
                return True
            if not minVal < root.val < maxVal:
                return False
            leftValid = isValid(root.left, minVal, min(maxVal, root.val))
            rightValid = isValid(root.right, max(minVal, root.val), maxVal)
            if leftValid and rightValid:
                return True
            return False
        return isValid(root, -1001, 1001)
        
        