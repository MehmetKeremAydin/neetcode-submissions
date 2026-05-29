"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        queue = deque()
        queue.append(node)
        seen = set()
        seen.add(node.val)
        newHeadNode = Node(node.val)
        ptr = {newHeadNode.val: newHeadNode}
        while(queue):
            node = queue.pop()
            curNode = ptr[node.val]
            for nghs in node.neighbors:
                if not nghs.val in seen:
                    seen.add(nghs.val)
                    queue.append(nghs)
                    newNode = Node(nghs.val)
                    ptr[nghs.val] = newNode
                    curNode.neighbors.append(newNode)
                else:
                    curNode.neighbors.append(ptr[nghs.val])
        return newHeadNode


        