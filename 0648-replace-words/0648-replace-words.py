class Solution:
    def replaceWords(self, dictionary: List[str], s1: str) -> str:
        
        s = set(dictionary)
        
        n = len(s1)
        
        ans = []
        l = 0
        while l < n:
            
            idx = l
            
            while idx < n and s1[idx] != " ":
                
                
                if s1[l:idx + 1] in s:
                    ans.append(s1[l:idx + 1])
                    
                    while idx < n:
                        if s1[idx] == " ":
                            break
                        idx += 1
                    break
                idx += 1
            else:
                ans.append(s1[l: idx])
            
            l = idx + 1
        return " ".join(ans)
            
        