class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        i = 1 
        
        while i < len(nums):
            prefix[i] = prefix[i-1] * nums[i-1]
            i += 1
        i = (len(nums) - 1) - 1    
        while i >= 0:
            postfix[i] = postfix[i+1] * nums[i + 1]
            i -= 1
        
        for i in range(len(nums)):
            nums[i] =  prefix[i] * postfix[i]
        
        return nums
            
            
            