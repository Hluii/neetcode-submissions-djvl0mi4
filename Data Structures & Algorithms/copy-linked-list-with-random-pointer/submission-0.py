"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = collections.defaultdict(lambda:Node(0))
        old[None] = None

        curr = head 
        while curr:
            old[curr].val = curr.val
            old[curr].next = old[curr.next]
            old[curr].random = old[curr.random]
            curr = curr.next
        return old[head]
                

