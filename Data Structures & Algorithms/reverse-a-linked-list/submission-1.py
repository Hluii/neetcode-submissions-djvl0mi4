# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # head is head detach and hold onto .next the set .next to be curr
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            # a b c 

