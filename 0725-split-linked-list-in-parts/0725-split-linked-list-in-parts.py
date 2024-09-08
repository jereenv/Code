# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        n = 0
        node = head
        
        while node:
            node = node.next
            n += 1
         
        r = n % k
        s = n // k
        
        ans = []
        
        for _ in range(k):
            size = s + (1 if r > 0 else 0)
            r -= 1
            
            ans.append(head)
            
            curr = head
            
            while size > 1:
                if curr:
                    curr = curr.next
                size -= 1
            
            if curr:
                head = curr.next
                curr.next = None
            
            
        return ans
                    
        