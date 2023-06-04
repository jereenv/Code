class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = 0
        
        q = []
        
        ans = []
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop(-1)
            q.append(r)
            
            if l > q[0]:
                q.pop(0)
            
            if r + 1 >= k:
                ans.append(nums[q[0]])
                l += 1
            
            r += 1
        return ans