# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init a dummy node with head as next
        dummy = ListNode(0, head)
        # Create a gap with left and right the size on len
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        # move left and right till right == None
        while right:
            left = left.next
            right = right.next
        # then set left.next = left.next.next
        left.next = left.next.next
        # return dummy.next
        return dummy.next