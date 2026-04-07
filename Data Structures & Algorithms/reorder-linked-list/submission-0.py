# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # have a defined length, travel throguh to grab then come back
        # travel to the end and count length

        # reverse half of the list?
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #reverse
        prev = None
        while second:
            dummy = second.next
            second.next = prev
            prev = second
            second = dummy
        # prev is head on secondlist
        l1,l2 = head, prev
        while prev:
            tprev = prev.next
            thead = l1.next
            l1.next = prev
            prev.next = thead
            l1 = thead
            prev = tprev
        return None

        # 2 4 
        # 6 8

            
        








