class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        s = bin(start)[2:]
        g = bin(goal)[2:]
        
        l1 = len(s)
        l2 = len(g)
        if l1 != l2:
            if l1 > l2:
                g = "0"*(l1 - l2) + g
            else:
                s = "0"*(l2 - l1) + s
        
        ans = 0
        for idx in range(max(l1, l2)):
            if s[idx] != g[idx]:
                ans += 1
        
        return ans
        