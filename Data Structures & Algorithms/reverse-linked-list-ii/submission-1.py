# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 0
        dummy = ListNode(0, head)
        preReverse = dummy
        while i < left-1:
            i += 1
            preReverse = preReverse.next
        i += 1
        leftNode = preReverse.next
        cur = leftNode
        prev = None
        while  i<= right:
            i += 1
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        preReverse.next = prev
        leftNode.next = cur
        return dummy.next
