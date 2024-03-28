class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        l, r = 0, 0
        n = len(nums)
        dic = {}
        
        while l <= r and r < n:
            dic[nums[r]] = 1 + dic.get(nums[r], 0)
            if dic[nums[r]] > k:
                while l <= r and dic[nums[r]] > k:
                    dic[nums[l]] -= 1
                    l += 1
            else:
                ans = max(ans, r - l + 1)
            r += 1
        
        return ans