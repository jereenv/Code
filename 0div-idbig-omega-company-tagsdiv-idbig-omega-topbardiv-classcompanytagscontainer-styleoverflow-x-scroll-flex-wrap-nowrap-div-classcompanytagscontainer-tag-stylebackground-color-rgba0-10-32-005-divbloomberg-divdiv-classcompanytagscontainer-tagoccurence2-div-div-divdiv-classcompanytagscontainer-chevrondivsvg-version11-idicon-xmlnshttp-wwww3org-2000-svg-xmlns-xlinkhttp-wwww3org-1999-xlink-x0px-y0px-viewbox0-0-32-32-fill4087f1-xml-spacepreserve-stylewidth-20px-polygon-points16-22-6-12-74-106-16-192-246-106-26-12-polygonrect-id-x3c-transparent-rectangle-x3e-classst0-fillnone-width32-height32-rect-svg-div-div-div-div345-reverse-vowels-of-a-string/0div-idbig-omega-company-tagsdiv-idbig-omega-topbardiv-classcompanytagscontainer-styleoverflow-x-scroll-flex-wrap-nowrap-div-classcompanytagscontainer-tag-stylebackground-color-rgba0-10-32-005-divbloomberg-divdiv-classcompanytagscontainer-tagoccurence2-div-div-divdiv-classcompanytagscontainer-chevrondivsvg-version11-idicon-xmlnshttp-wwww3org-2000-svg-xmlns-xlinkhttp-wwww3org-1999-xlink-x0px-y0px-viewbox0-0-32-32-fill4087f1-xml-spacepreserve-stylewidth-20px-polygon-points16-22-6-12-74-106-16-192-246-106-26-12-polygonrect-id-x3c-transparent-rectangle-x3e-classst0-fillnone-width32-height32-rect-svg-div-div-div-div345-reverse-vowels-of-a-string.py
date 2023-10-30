class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = 'aeiouAEIOU'
        v_stack = []
        ans = ""
        
        for c in s:
            if c in vowels:
                v_stack.append(c)
        
        for c in s:
            if c in vowels:
                ans += v_stack.pop()
            else:
                ans += c
        
        return ans
                     
            
        