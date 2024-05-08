class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        inverse = [-1 for i in range(10**6)]
        
        for idx, val in enumerate(score):
            inverse[val] = idx
        
        ans = [-1 for i in range(len(score))]
        
        medals = ["Bronze Medal","Silver Medal","Gold Medal"]

        curr = 1
        for idx in reversed(inverse):
            if idx != -1:
                if curr < 4:
                    ans[idx] = medals.pop()
                else:
                    ans[idx] = str(curr)
                curr += 1
        
        return ans
                    
        
        
        