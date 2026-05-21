# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        structure = dict()
        for i, num in enumerate(inorder):
            structure[num] = i
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            cur = root
            tbi = preorder[i]
            tbi_idx = structure[tbi]
            while(True):
                cur_idx = structure[cur.val]
                if cur_idx > tbi_idx:
                    if cur.left:
                        cur = cur.left
                        continue
                    cur.left = TreeNode(tbi)
                    break
                else:
                    if cur.right:
                        cur = cur.right
                        continue
                    cur.right = TreeNode(tbi)
                    break
        return root



        