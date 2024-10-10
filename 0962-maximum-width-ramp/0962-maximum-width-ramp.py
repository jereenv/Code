class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        t = [x for x in range(n)]
        
        t.sort(key = lambda i: (nums[i], i))
        
        m1 = n
        ans = 0
        
        for idx in t:
            ans = max(ans, idx - m1)
            m1 = min(m1, idx)
        
        return ans
        