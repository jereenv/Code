# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        ans, node = 0, head
        
        while node:
            if node.val > node.next.val:
                ans += 1
            else:
                ans -= 1
            node = node.next.next
            
        return "Even" if ans > 0 else "Tie" if ans == 0 else "Odd"
        