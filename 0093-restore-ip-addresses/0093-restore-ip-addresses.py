class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not (3 < len(s) < 13):
            return []
        
        ans = []
        def backtrack(idx, dot, currIP):
            if dot == 4 and idx == len(s):
                ans.append(currIP[:-1])
            
            
            if dot > 4:
                return
            
            for j in range(idx, min(idx + 3, len(s))):
                if int(s[idx:j + 1]) < 256 and (idx == j or s[idx] != "0"):
                    backtrack(j + 1, dot + 1, currIP + s[idx:j+1] + ".")
        
        
        backtrack(0,0,"")
        
        return ans
    