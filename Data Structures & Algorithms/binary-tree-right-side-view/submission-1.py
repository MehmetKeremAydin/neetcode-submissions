# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()
        queue = deque([root])
        answer = []
        while(queue):
            num_count = len(queue)
            for i in range(num_count):
                node = queue.popleft()
                if i==0:
                    answer.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return answer


        