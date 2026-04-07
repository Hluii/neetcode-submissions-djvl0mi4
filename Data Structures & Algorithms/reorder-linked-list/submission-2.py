# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast slow to find 2nd half
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse it
        prev = None
        while second:
            dummy = second.next
            second.next = prev
            prev = second
            second = dummy
        # prev is now head of reversed half list
        while prev:
            thead, tprev = head.next, prev.next
            head.next = prev
            prev.next = thead
            head = thead
            prev = tprev
        return None

        