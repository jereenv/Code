class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ans_len = 0
        n = len(s)
        for idx in range(len(s)):
            
            #odd length palindrome
            l, r = idx, idx
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > ans_len:
                    ans = s[l:r+1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
                
            #even length palindrom
            l, r = idx, idx + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
        return ans
                    