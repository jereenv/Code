class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
#         n = len(nums)
        
#         for i in range(n):
#             if nums[i] < 0:
#                 nums[i] = 0
        
        
#         for i in range(n):
#             num = abs(nums[i])
#             if 0 < num < n + 1:
                
#                 if nums[num - 1] > 0:
#                     nums[num - 1] *= -1
#                 elif nums[num - 1] == 0:
#                     nums[num - 1] = -1 * (n + 1)
                
        
#         for i in range(1, n + 1):
#             if nums[i - 1] > 0:
#                 return i
        
#         return n + 1

        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
            
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
            
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1