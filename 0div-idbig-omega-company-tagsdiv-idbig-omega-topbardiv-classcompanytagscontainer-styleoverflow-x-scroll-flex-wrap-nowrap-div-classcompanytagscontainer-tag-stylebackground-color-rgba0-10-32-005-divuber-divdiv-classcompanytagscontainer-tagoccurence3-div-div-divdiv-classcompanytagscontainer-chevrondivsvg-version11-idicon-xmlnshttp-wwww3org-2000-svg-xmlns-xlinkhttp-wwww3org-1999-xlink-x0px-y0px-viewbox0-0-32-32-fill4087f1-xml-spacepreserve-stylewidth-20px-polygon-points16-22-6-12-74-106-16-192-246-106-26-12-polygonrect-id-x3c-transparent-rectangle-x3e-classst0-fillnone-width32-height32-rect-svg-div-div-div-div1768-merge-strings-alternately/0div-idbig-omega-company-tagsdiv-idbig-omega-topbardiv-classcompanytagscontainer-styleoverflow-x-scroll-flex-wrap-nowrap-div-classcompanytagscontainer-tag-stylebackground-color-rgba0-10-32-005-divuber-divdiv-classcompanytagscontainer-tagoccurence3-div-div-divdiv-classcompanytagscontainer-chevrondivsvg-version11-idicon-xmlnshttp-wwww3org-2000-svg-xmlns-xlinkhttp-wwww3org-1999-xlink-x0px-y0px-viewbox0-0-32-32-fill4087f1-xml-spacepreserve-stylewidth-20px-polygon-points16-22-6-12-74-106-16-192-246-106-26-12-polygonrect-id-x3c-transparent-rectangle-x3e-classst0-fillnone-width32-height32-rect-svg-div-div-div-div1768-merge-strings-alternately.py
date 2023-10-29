class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        m, n = len(word1), len(word2)
        ans = ""
        while l < m or l < n:
            if l < m:
                ans += word1[l]            
            if l < n:
                ans += word2[l]
            l+= 1
        
        return ans
                
        