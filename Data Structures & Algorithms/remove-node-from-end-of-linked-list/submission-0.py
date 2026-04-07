# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # intialize a dummy node with next to ehad
        dummy = ListNode(0, head)
        # make a gap the size of n with left and right
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        # push left and right pointer right until right reaches the end
        while right:
            right = right.next
            left = left.next
        # set left.next to left.next.next?
        left.next = left.next.next
        # return dummy.next which is head
        return dummy.next