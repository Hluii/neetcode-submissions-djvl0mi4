# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # cut into half with slow and fast
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy
        # combine
        while prev:
            tprev = prev.next
            thead = head.next
            head.next = prev
            prev.next = thead
            prev = tprev
            head = thead
        return None
