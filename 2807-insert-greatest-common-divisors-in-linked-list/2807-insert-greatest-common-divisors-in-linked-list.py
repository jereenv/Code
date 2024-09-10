# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            if(b == 0):
                return abs(a)
            else:
                return gcd(b, a % b)
        
        node = head
        while node.next:
            a = node.val
            b = node.next.val
            c = gcd(a, b)
            
            n = node.next
            node.next = ListNode(val = c, next = n)
            
            node = n
        
        return head