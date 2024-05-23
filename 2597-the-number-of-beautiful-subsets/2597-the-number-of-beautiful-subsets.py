class Solution:
    
    ans = -1
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        
        dic = defaultdict(int)
        n = len(nums)
        
        def backtrack(idx, curr):
            if idx == n:
                self.ans += 1
                return
            
            backtrack(idx + 1, curr.copy())
            
            if curr[nums[idx] - k] == 0 and curr[nums[idx] + k] == 0:
                curr[nums[idx]] += 1
                backtrack(idx + 1, curr.copy())
            
            
        backtrack(0, dic)
        return self.ans
        