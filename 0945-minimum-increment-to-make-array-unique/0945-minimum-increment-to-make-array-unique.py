class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        ans = 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                ans += nums[idx - 1] - nums[idx] + 1
                nums[idx] = nums[idx - 1] + 1
        
        return ans
        