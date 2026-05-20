# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKNodes(self, head, k) -> (ListNode, ListNode):
        cur = head
        prev = None
        for i in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return (prev, head) # head, tail
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        ptrR, ptrL = dummyNode, dummyNode
        memory = ptrL.next
        counter = 0
        for i in range(k+1):
            ptrR = ptrR.next
        while((ptrR or counter % k == 0) and memory):
            if counter % k == 0:
                rHead, rTail = self.reverseKNodes(memory, k)
                #print(rHead.val, rTail.val)
                ptrL.next = rHead
                rTail.next = ptrR
                memory = ptrR
            counter += 1
            if ptrR:
                ptrR = ptrR.next
            ptrL = ptrL.next
        return dummyNode.next

        