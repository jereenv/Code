"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = [root]
        while len(nodes):
            level = []
            for i in nodes:
                if i:
                    if i.left:
                        level.append(i.left)
                        level.append(i.right)
            for i in range(len(level) - 1):
                level[i].next = level[i+1]
            nodes = level
        return root
        