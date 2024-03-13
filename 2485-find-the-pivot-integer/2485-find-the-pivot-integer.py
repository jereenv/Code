class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 1, n
        s1, s2 = 0, 0
        while l != r:
            if s1 < s2:
                s1 += l
                l += 1
            else:
                s2 += r
                r -= 1
        return l if s1 == s2 else -1
        
        