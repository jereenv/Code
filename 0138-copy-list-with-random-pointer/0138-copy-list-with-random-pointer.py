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
        
        linkedMap = {None : None}
        
        temp = head
        while temp:
            node = Node(temp.val)
            linkedMap[temp] = node
            temp = temp.next
        
        temp = head
        while temp:
            node = linkedMap[temp]
            node.next = linkedMap[temp.next]
            node.random = linkedMap[temp.random]
            temp = temp.next
        
        return linkedMap[head]
        
        