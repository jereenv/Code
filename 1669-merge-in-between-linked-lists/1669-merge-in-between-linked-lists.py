# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        tail2 = list2
        
        while tail2.next:
            tail2 = tail2.next
        
        node1 = list1
        
        a -= 1
        while a > 0:
            node1 = node1.next 
            a -= 1
            b -= 1
        
        
        temp = node1.next
        node1.next = list2
        
        node1 = temp
        
        
        while b > 0:
            node1 = node1.next
            b -= 1
        
        tail2.next = node1
        
        return list1
        
            
        