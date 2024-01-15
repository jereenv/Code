class Solution:
    
    def compare(self, s1, s2):
        
        idx = 0
        while idx < len(s1) and idx < len(s2):
            if s1[idx] != s2[idx]:
                break
            idx += 1
        return s2[:idx]
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]
        
        for i in range(1, len(strs)):
            prev = self.compare(prev, strs[i])
            if prev == -1:
                return ""
        
        
        
        return prev