class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        
        n = len(s)
        
        res = []
        
        def backtrack(start, end, ans):
            if end >= n:
                if s[start: end] in wordSet:
                    if ans:
                        res.append(ans[1:] + " " + s[start : end])
                    else:
                        res.append(s[start : end])
                return
            
            if s[start: end] in wordSet:
                backtrack(end, end + 1, ans + " " + s[start : end])
            
            backtrack(start, end + 1, ans)
        
        backtrack(0, 0, "")
        
        return res
            
        