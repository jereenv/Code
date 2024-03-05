# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        vis = set()
        while headA:
            vis.add(headA)
            headA = headA.next
        
        while headB:
            if headB in vis:
                return headB
            headB = headB.next
        
 
        