class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        
        if len(original) != m * n:
            return []
        
        array = [[0] * n for _ in range(m)]
        
        index = 0
        
        for i in range(0, m):
            for j in range(n):
                array[i][j] = original[index]
                index += 1
        
        return array
        