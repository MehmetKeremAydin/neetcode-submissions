# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def postOrder(node):
            if node == None:
                return True
            delL = postOrder(node.left)
            delR = postOrder(node.right)
            if delL and delR and node.val == target:
                del node
                return True
            else:
                node.left = None if delL == True else node.left
                node.right = None if delR == True else node.right
                return False
        dummyNode = TreeNode(0, root, None)
        postOrder(dummyNode)
        return dummyNode.left