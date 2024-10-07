class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []
        
        n = len(s)
        idx = 0
        
        
        while idx < n:
            if stack and ((s[idx] == "D" and stack[-1] == "C") or (s[idx] == "B" and stack[-1] == "A")):
                    stack.pop()
                    
            else:
                stack.append(s[idx])
            idx +=1
        
        return len(stack)