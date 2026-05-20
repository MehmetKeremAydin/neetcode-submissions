# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeSorted(self, head1:ListNode, head2:ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while(head1 and head2):
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        tail = head1 if head1 else head2
        cur.next = tail
        return dummy.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flag = False
        while(len(lists) > 1):
            flag = True
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            combined = self.mergeSorted(list1, list2)
            lists.append(combined)
        if flag:
            return lists[0]

        