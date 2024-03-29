class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0,0
        
        n = len(nums)
        ans = 0
        
        c = 0
        
        m = max(nums)
        
        while l <= r:
            if c < k:
                if r >= n:
                    break
                if nums[r] == m:
                    c += 1
                r += 1
            else:
                ans += n -r + 1
                
                if nums[l] == m:
                    c -=1
                l += 1
        
        return ans
            
            
                    
                
            