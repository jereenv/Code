class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0,0
        
        n = len(nums)
        ans = 0
        
        dic = defaultdict(int)
        
        m = max(nums)
        
        while l <= r:
            if dic[m] < k:
                
                if r >= n:
                    break
                dic[nums[r]] += 1
                r += 1
            else:
                ans += n -r + 1
                dic[nums[l]] -= 1
                l += 1
        
        return ans
            
            
                    
                
            