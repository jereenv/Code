class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        
        right = len(nums) - 1
        left = right - 1
        
        curr_sum = 0
        
        count = 1
        target_sum = nums[right]
        curr_sum = target_sum
        while left >= 0:
            curr_sum += nums[left]
            if curr_sum + k >= nums[right] * (right - left + 1):
                left -= 1
            else:
                curr_sum -= nums[right]
                right -= 1
                left -= 1
            ans = max(ans, right - left)
        return ans
                
        