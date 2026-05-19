# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head:Optional[ListNode]) -> ListNode:
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        fastPtr = head.next
        slowPtr = head
        while(fastPtr and fastPtr.next):
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
            if fastPtr:
                fastPtr = fastPtr.next
        head2 = self.reverseList(slowPtr.next)
        slowPtr.next = None
        curL = head
        curR = head2
        while(curR):
            tempL = curL.next
            tempR = curR.next
            curL.next = curR
            curR.next = tempL
            curL = tempL
            curR = tempR
            


            
        
        

