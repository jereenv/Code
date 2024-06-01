class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for idx in range(1, len(s)):
            res += abs(ord(s[idx - 1]) - ord(s[idx]))
        
        return res
        