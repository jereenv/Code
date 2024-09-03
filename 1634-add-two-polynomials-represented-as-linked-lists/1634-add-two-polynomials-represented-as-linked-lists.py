# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        dummy = PolyNode()
        
        curr = dummy
        
        while poly1 and poly2:
            if poly1.power > poly2.power:
                curr.next = PolyNode(x = poly1.coefficient, y = poly1.power)
                curr = curr.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                curr.next = PolyNode(x = poly2.coefficient, y = poly2.power)
                curr = curr.next
                poly2 = poly2.next
            else:
                s = poly2.coefficient + poly1.coefficient
                if s!= 0:
                    curr.next = PolyNode(x = s, y = poly2.power)
                    curr = curr.next
                poly2 = poly2.next            
                poly1 = poly1.next
        
        while poly1:
            curr.next = poly1
            curr = curr.next
            poly1 = poly1.next
        
        
        while poly2:
            curr.next = poly2
            curr = curr.next
            poly2 = poly2.next
        
        return dummy.next
        
        
        