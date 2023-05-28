class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        def getS(s):
            
            res = ""
            hash = 0
            for i in range(len(s)-1, -1 , -1):
                
                if s[i] == "#":
                    hash += 1
                    continue
                if hash == 0:
                    res = s[i] + res
                else:
                    hash -= 1
            
            return res
        
        return getS(s) == getS(t)

                    
