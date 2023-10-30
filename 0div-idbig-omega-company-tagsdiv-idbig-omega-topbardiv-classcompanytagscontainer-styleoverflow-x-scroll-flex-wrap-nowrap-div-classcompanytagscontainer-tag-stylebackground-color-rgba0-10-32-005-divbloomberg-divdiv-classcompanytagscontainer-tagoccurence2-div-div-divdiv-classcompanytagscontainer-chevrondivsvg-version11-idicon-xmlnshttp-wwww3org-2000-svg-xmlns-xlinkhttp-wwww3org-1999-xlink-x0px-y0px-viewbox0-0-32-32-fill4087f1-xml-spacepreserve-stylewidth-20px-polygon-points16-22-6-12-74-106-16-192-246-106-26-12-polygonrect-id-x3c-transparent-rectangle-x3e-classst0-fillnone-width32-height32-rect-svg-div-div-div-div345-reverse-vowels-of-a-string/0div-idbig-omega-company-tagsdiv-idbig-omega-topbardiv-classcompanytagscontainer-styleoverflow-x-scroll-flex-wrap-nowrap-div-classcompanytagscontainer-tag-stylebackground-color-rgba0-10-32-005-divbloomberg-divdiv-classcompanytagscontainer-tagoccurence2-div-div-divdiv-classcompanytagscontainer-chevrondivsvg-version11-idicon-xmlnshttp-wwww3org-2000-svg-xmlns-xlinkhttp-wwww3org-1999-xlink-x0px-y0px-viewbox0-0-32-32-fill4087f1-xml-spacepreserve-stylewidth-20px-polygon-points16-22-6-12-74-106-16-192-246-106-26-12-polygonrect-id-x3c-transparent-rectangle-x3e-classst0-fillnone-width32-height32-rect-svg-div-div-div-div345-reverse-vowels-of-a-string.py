class Solution:
    def reverseVowels(self, s: str) -> str:
        
        l, r = 0, len(s) - 1
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while l < r:
            if s[l].lower() in vowels:
                while s[r].lower() not in vowels:
                    r-= 1
                
                s[l], s[r] = s[r], s[l]
                r -= 1
        
            l += 1
        
        return "".join(s)
                     
            
        