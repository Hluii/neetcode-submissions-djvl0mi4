# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen_dict = {}
        while curr:
            if curr not in seen_dict:
                seen_dict[curr] = 1
            else:
                return True
            curr = curr.next
        return False