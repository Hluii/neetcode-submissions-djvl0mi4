# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_list = {}
        curr = head
        while curr:
            if curr in seen_list:
                return True
            else:
                seen_list[curr] = 1
            curr = curr.next
        return False