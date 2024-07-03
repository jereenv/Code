class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()
        
        print(nums)
        return min(abs(nums[2] - nums[-2]), abs(nums[1] - nums[-3]), abs(nums[3] - nums[-1]), abs(nums[-4] - nums[0]))
        
        
        