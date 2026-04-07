# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # create a reversed list by using fast slow to find mid point
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # cut off slow
        # then from second reverse
        prev = None
        while second:
            dummy = second.next
            second.next = prev
            prev = second
            second = dummy
        # prev is head of the reversed half list
        while prev:
            temph, tempp = head.next, prev.next
            head.next = prev
            prev.next = temph
            head = temph
            prev = tempp
        return None

        # then join two lists
