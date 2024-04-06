class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        l, r = 0, 0
        
        ans = []
        for i in s:
            if i != ")":
                ans.append(i)
                
                if i == "(":
                    l += 1
                
            else:
                if l > 0:
                    ans.append(i)
                    l -= 1
        
        for i in range(len(ans) - 1, -1, -1):
            if l <= 0:
                break
            
            if ans[i] == "(":
                ans.pop(i)
                l -= 1
        
        return "".join(ans)
            
            
        