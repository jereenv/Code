# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        critic = []
        curr = head
        
        idx = 0
        while curr.next.next:
            if (curr.next.val > curr.val and curr.next.val > curr.next.next.val) or (curr.next.val < curr.val and curr.next.val < curr.next.next.val):
                critic.append([idx, curr.next.val])
            idx += 1
            curr = curr.next
        
        mi, ma = 10**5, 0
        
        if len(critic) < 2:
            return [-1, -1]
        
        print(critic)
        for idx in range(len(critic) - 1):
            #if critic[idx][1] != critic[idx + 1][1]:
            mi = min(mi, critic[idx +1][0] - critic[idx][0])
            #ma = max(ma, critic[idx +1][0] - critic[idx][0])
        
        return [mi, critic[-1][0] - critic[0][0]]