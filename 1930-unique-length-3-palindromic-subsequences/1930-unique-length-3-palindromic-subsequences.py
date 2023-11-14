class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        final = set()
        vis = set()
        
        n =  len(s) - 1
        
        for i in range(len(s)):
            l, r = i, n
            
            if s[l] not in vis:
                while l < r:
                    if s[r] != s[l]:
                        r -= 1
                    else:
                        s1 = set(list(s[l+1:r]))
                        for letter in s1:
                            final.add(s[l] + letter + s[r])

                        break
                vis.add(s[l])
            
        #print(final)
        return len(final)