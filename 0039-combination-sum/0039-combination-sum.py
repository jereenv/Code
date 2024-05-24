class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        n = len(candidates)
        
        
        res = []
        
        def backtrack(idx, curr, combi):
            if idx == n:
                return
            
            if curr > target:
                return
            
            if curr == target:
                res.append(combi)
                return
            
            if curr + candidates[idx] > target:
                return
            
            backtrack(idx, curr + candidates[idx], combi + [candidates[idx]])
            
            backtrack(idx + 1, curr, combi)
        
        backtrack(0, 0, [])
        
        return res
            
            
        
            
        