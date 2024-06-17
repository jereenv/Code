class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        cs = int(c ** 0.5)
        
#         s = set()
#         for i in range(cs + 1):
#             s.add(i**2)
        
#         for i in range(cs + 1):
#             if (c - i**2) in s:
#                 return True
        
#         return False

        
        l, r = 0, cs
        
        while l <= r:
            t = l**2 + r**2
            if t == c:
                return True
            elif t > c:
                r -= 1
            else:
                l += 1
        return False
                
        