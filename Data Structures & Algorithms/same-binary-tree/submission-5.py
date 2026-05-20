# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameNode(self, a:TreeNode, b:TreeNode) -> bool:
        if (a.val != b.val):
            return False
        elif(((a.left!=None) ^ (b.left!=None)) or ((a.right!=None) ^ (b.right!=None))):
            return False
        else: 
            return True
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p==None or q==None):
            return not ((p==None) ^ (q==None))
        pStack, qStack = [p], [q]
        while(pStack and qStack):
            pNode = pStack.pop()
            qNode = qStack.pop()
            if not self.isSameNode(pNode, qNode):
                return False
            if pNode.left:
                pStack.append(pNode.left)
                qStack.append(qNode.left)
            if pNode.right:
                pStack.append(pNode.right)
                qStack.append(qNode.right)
        if len(pStack) != 0 and len(qStack) != 0:
            return False
        return True

             