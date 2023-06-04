class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        sCount = {}
        
        for i in t:
            tCount[i] = 1 + tCount.get(i,0)
        
        l = 0
        
        have = 0
        need = len(tCount)
        
        ansLen = float('infinity')
        ans = [-1,-1]
        
        for r in range(len(s)):
            
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            if (s[r] in tCount) and (tCount[s[r]] == sCount[s[r]]):
                have += 1
            
            while have == need:
                if (r - l + 1) < ansLen:
                    ansLen = r - l  + 1
                    ans = [l, r + 1]
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -=1
                
                l += 1
        
        l,r = ans
        return s[l: r]