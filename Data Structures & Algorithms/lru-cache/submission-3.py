class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.dummy_head = ListNode(0, 0)
        self.capacity = capacity
        self.far_ptr = self.dummy_head

    def removeNode(self, item):
        if self.far_ptr == item:
            self.far_ptr = item.prev
        next_node = item.next
        prev_node = item.prev
        if next_node:
            next_node.prev = prev_node
        if prev_node:
            prev_node.next = next_node
    
    def insertNode(self, head, item):
        head_next = head.next
        if head_next:
            head_next.prev = item
        head.next = item
        item.next = head_next
        item.prev = head
        if self.far_ptr == self.dummy_head:
            self.far_ptr = item
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.insertNode(self.dummy_head, node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.key = key
            self.removeNode(node)
            self.insertNode(self.dummy_head, node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insertNode(self.dummy_head, node)
            if len(self.cache) > self.capacity:
                self.cache.pop(self.far_ptr.key)
                self.removeNode(self.far_ptr)



            

