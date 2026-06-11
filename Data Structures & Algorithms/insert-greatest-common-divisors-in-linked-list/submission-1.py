# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findGCD(num1:int, num2:int) -> int:
            while num2 > 0:
                num1, num2 = num2, num1 % num2
            return num1
        cur = head
        while cur.next:
            newNode = ListNode(findGCD(cur.val, cur.next.val), cur.next)
            cur.next = newNode
            cur = cur.next.next
        return head
        
