class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        
        row = (top + bottom)//2
        
        while top <= bottom:
            if matrix[row][right] < target:
                top = row + 1
            elif matrix[row][left] > target:
                bottom = row - 1
            else:
                break
            row = (top + bottom)//2
        
        if top > bottom:
            return False
        
        cols = (left + right)//2
        while left <= right:
            if matrix[row][cols] < target:
                left = cols + 1
            elif matrix[row][cols] > target:
                right = cols - 1
            else:
                return True
            cols = (left + right)//2
        return False
                
        
        