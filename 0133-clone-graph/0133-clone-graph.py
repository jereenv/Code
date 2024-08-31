"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def clone(self, neighbours, clone_node):
        if neighbours:
            clone_node.neighbors = []
        for node in neighbours:
            if node.val not in self.vis:
                self.vis[node.val] = Node(val = node.val)
                self.clone(node.neighbors, self.vis[node.val])
            clone_node.neighbors.append(self.vis[node.val])


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        self.vis = {}
        head = Node(val = node.val, neighbors = node.neighbors)
        
        self.vis[node.val] = head

        self.clone(node.neighbors, head)

        return head

