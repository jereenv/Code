class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        l, r = 0, 0
        n = len(nums)
        dic = {}
        
        while l <= r and r < n:
            dic[nums[r]] = 1 + dic.get(nums[r], 0)

            ans = max(ans, r - l)
            while l <= r and dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l += 1
            r += 1
        
        if dic[nums[r -1]] <= k:
            ans = max(ans, r - l)
        
        return ans