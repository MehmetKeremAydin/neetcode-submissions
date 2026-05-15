# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next = head
        while (next != None):
            cur = next
            next = cur.next
            cur.next = prev
            prev = cur
        return prev
    
    def reverList_rec(self, cur: Optional[ListNode], prev:Optional[ListNode]):
        if cur == None:
            return None
        if cur.next != None:
            head = self.reverList_rec(cur.next, cur)
        else:
            head = cur
        cur.next = prev
        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverList_rec(head, None)