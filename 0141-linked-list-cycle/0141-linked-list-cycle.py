# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        nodes = set()
        slow  = head
        fast = head
        while slow:
            if slow in nodes:
                return True
            nodes.add(slow)
            slow = slow.next
        return False
        