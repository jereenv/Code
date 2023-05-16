# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        while list1 != None or list2 != None:
            if list1 == None:
                temp.next = list2
                return head.next
            
            if list2 == None:
                temp.next = list1
                return head.next
            
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        return head.next
                
        