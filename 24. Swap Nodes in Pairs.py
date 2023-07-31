# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        nexthead = head.next.next
        newhead = head.next
        newhead.next = head
        head.next = self.swapPairs(nexthead)
        return newhead
