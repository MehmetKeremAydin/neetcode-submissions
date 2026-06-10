# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        def DFS(node):
            if node == None:
                return
            DFS(node.left)
            DFS(node.right)
            postorder.append(node.val)
        DFS(root)
        return postorder