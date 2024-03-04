# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        ans = 0
        
        while head:
            ans += (head.val > head.next.val) - (head.val < head.next.val)
            head = head.next.next
        return "Even" if ans > 0 else "Tie" if ans == 0 else "Odd"
        