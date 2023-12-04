class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans  = -1
        while l < r:
            if nums[l] + nums[r] < k:
                ans = max(nums[l] + nums[r], ans)
                l += 1
            else:
                r -= 1
        return ans 
        
        