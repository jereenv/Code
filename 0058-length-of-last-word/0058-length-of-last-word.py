class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        n = len(s)
        while l < n and s[-1 - l] == " " :
            l += 1
        
        ans = 0
        while l < n and s[-1 - l] != " "  :
            l += 1
            ans += 1
        
        return ans