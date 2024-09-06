# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        
        dummy = ListNode(next = head)
        
        curr = dummy
        
        
        while curr.next:
            if curr.next.val not in nums:
                curr = curr.next
            else:
                curr.next = curr.next.next
        
        
        return dummy.next
        