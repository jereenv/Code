# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(i):
            if i + 1 < len(lists):
                dummy = ListNode()
                l1 = lists[i]
                l2 = lists[i+1]
                curr = dummy
                while l1 and l2:
                    if l1.val > l2.val:
                        curr.next = l2
                        l2 = l2.next
                    else:
                        curr.next = l1
                        l1 = l1.next
                    
                    curr = curr.next
                
                if l1:
                    curr.next = l1
                if l2:
                    curr.next = l2
                
                lists[i] = dummy.next
        
        def newL():
            newArr = []
            for i in range(len(lists)):
                if i % 2 == 0 :
                    newArr.append(lists[i])
            return newArr
        
        while len(lists) > 1:
            for i in range(0,len(lists),2):
                merge(i)
            
            lists = newL()
        
        return lists[0] if len(lists) > 0 else None 
       
            
            
        