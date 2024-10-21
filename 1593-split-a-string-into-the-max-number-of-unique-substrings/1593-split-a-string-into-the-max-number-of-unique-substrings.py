class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        seen = set()
        n = len(s)
        
        def backtrack(start):
            if start == n:
                return 0
            
            max_count = 0 
            
            for end in range(start + 1, n + 1):
                substring = s[start: end]
                
                if substring not in seen:
                    seen.add(substring)
                    max_count = max(max_count, 1 + backtrack(end))
                    seen.remove(substring)
            
            return max_count
    
        
        return backtrack(0)