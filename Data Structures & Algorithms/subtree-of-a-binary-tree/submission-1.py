# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqualTree(self, a:TreeNode, b:TreeNode) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        
        return self.isEqualTree(a.left, b.left) and self.isEqualTree(a.right, b.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if self.isEqualTree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False