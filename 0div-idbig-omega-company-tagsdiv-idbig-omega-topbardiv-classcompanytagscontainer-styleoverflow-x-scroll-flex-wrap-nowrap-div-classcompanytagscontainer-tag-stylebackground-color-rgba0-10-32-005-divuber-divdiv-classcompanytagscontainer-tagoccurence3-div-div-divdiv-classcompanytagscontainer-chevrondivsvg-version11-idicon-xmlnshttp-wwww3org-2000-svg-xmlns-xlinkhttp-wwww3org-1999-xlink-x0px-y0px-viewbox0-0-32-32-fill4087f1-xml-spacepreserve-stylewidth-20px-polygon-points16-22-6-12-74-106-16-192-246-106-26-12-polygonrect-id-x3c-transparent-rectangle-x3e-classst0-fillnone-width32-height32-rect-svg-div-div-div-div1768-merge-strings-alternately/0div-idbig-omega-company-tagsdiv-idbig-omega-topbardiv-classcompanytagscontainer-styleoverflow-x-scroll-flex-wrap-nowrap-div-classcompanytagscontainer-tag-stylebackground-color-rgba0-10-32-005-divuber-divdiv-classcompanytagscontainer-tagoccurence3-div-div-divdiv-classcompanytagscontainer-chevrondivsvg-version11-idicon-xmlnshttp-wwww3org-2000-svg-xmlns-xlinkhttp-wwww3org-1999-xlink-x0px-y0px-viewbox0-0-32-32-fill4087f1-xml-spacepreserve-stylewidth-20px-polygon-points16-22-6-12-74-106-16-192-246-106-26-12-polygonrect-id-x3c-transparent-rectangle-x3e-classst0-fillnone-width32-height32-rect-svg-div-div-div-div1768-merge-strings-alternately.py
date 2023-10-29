class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        m, n = len(word1), len(word2)
        ans = ""
        while l < m or r < n:
            if l < m:
                ans += word1[l]
                l += 1
            
            if r < n:
                ans += word2[r]
                r+= 1
        
        return ans
                
        