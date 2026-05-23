# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        stack = [(root, 0, 0)]
        answer = ""
        while stack:
            node, level, loc = stack.pop()
            answer += "#" + str(node.val) + "_" + str(level) + "_" + str(loc)
            if node.left:
                stack.append([node.left, level+1, 2*loc])
            if node.right:
                stack.append([node.right, level+1, 2*loc+1])
        return answer
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return
        treeNodes = dict()
        data = data.split("#")[1:]
        queue = deque()
        for entry in data:
            entry = entry.split("_")
            treeNodes[(int(entry[1]), int(entry[2]))] = int(entry[0])
        head = TreeNode(treeNodes[(0,0)])
        queue.append((0,0,head))
        print(treeNodes)
        while queue:
            level, loc, node = queue.popleft()
            if (level+1, 2*loc) in treeNodes:
                node.left = TreeNode(treeNodes[(level+1, 2*loc)])
                queue.append((level+1, 2*loc, node.left))
            if (level+1, 2*loc+1) in treeNodes:
                node.right = TreeNode(treeNodes[(level+1, 2*loc+1)])
                queue.append((level+1, 2*loc+1, node.right))
        return head



            