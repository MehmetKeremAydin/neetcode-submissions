# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        curSum = dummy
        overflow = 0
        while(cur1 and cur2):
            sum = cur1.val + cur2.val + overflow
            overflow = sum // 10
            curSum.next = ListNode(sum%10)
            cur1 = cur1.next
            cur2 = cur2.next
            curSum = curSum.next
        cur = cur1 if cur1 else cur2
        while(cur and overflow):
            sum = cur.val + overflow
            overflow = sum // 10
            curSum.next = ListNode(sum%10)
            cur = cur.next
            curSum = curSum.next
        if cur:
            curSum.next = cur
        if overflow:
            curSum.next = ListNode(overflow)
        return dummy.next

        