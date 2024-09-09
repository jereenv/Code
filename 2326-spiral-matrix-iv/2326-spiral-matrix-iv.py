# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        row = 0
        col = 0
        
        matrix = [[-1] * n for _ in range(m)]
        
        curr = head
        
        while curr:
            
            for idx in range(col, n):
                if not curr:
                    break
                matrix[row][idx] = curr.val
                curr = curr.next
            
            row += 1
            
            for idx in range(row, m):
                if not curr:
                    break
                matrix[idx][n - 1] = curr.val
                curr = curr.next
            n -= 1
            
            for idx in range(n - 1, col - 1, -1):
                if not curr:
                    break
                matrix[m - 1][idx] = curr.val
                curr = curr.next
            m -= 1
            
            for idx in range(m - 1, row - 1, -1):
                if not curr:
                    break
                matrix[idx][col] = curr.val
                curr = curr.next
            
            col += 1
        
        return matrix
            
        