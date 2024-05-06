# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        
        while node:
            stack.append(node)
            node = node.next
        
        
        idx = -2
        
        #print([node.val for node in stack])
        while idx*(-1) <= len(stack):
            if stack[idx].val < stack[idx + 1].val:
                stack.pop(idx)
                #print(stack.pop(idx).val)
            else:
                idx -= 1
        
        dummy = ListNode()
        node = dummy
        
        for i in stack:
            node.next = i
            node = i
        
        node = None
        
        return dummy.next
            
        