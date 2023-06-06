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
        
        linkedMap = {}
        
        temp = head
        while temp:
            node = Node(temp.val)
            linkedMap[temp] = node
            temp = temp.next
        
        temp = head
        while temp:
            node = linkedMap[temp]
            if temp.next:
                node.next = linkedMap[temp.next]
            if temp.random:
                node.random = linkedMap[temp.random]
            temp = temp.next
        
        return linkedMap[head] if head else None
        
        
        