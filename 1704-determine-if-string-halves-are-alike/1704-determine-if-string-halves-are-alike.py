class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        mid = (len(s) + 1)//2
        idx = 0
        ctr = 0
        while idx < mid:
            if s[idx] in vowels:
                ctr += 1
            if s[idx + mid] in vowels:
                ctr -= 1
            idx += 1
        
        return ctr == 0