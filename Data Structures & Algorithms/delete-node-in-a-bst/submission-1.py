# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummyNode = TreeNode(100001, root, None)
        cur = dummyNode
        while cur:
            if cur.val < key:
                if cur.right:
                    if cur.right.val == key:
                        pRoot = cur
                        tbr = cur.right
                        break
                    else:
                        cur = cur.right
                else:
                    return root
            else:
                if cur.left:
                    if cur.left.val == key:
                        pRoot = cur
                        tbr = cur.left
                        break
                    else:
                        cur = cur.left
                else:
                    return root
        if cur == None:
            return root
        if tbr.left:
            if tbr.val < pRoot.val:
                pRoot.left = tbr.left
            else:
                pRoot.right = tbr.left
            cur = tbr.left
            append = tbr.right
            del tbr
            while cur.right:
                cur = cur.right
            cur.right = append
        else:
            if tbr.val < pRoot.val:
                pRoot.left = tbr.right
            else:
                pRoot.right = tbr.right
            del tbr
        return dummyNode.left
