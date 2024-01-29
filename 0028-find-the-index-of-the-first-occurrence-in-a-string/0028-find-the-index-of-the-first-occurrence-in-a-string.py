class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        idx = 0
        
        while idx < len(haystack):
            if haystack[idx] == needle[0]:
                temp = 0
                while idx + temp < len(haystack) and temp < len(needle) and haystack[idx + temp] == needle[temp]:
                    temp += 1
                if temp == len(needle):
                    return idx
                
            idx += 1
        return -1
        