# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # make a gap, then move it to the end, fix next, return head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while right and n > 0: # makes a gap the size of n
            right = right.next
            n -= 1
        while right:# move righ to the end with the gap between left 
            right = right.next
            left = left.next
        left.next = left.next.next # skip the next value to remove
        return dummy.next