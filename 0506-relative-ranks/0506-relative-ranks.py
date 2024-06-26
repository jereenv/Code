class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        m = 0
        for i in score:
            m = max(i, m)
        
        inverse = [-1 for i in range(m + 1)]
        
        for idx, val in enumerate(score):
            inverse[val] = idx
        
        ans = [-1 for i in range(len(score))]
        
        medals = ["Bronze Medal","Silver Medal","Gold Medal"]

        curr = 1
        for idx in reversed(inverse):
            if idx != -1:
                if curr < 4:
                    ans[idx] = medals[-curr]
                else:
                    ans[idx] = str(curr)
                curr += 1
        
        return ans
                    
        
        
        