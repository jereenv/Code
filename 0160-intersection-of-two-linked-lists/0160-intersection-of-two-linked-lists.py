# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def getLen(node):
            ctr = 0
            while node:
                ctr += 1
                node = node.next
            return ctr

        lenA, lenB = getLen(headA), getLen(headB)

        node1, node2 = headA, headB

        for _ in range(abs(lenA - lenB)):
            if lenA > lenB:
                node1 = node1.next
            else:
                node2 = node2.next
        
        while node1:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        
 
        