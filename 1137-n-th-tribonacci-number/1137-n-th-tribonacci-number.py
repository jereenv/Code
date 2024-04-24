class Solution:
    def tribonacci(self, n: int) -> int:
        
        first = 0
        second = 1
        third = 1
        
        if n == 0:
            return first
        if n == 1:
            return second
        if n == 2:
            return third
        
        for _ in range(3, n):
            temp = third
            
            third = first + second + third
            first, second = second, temp
        
        return first + second + third
        