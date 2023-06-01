class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
    
        l = 0
        freq = {}
        ans = 0
        for r in range(len(s)):
            if not s[r] in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            
            replace = (r - l + 1) - max(freq.values())
            
            if replace <= k:
                ans = max(ans, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return ans
                