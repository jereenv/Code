class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        i = len(nums) - 1
        if i == 0:
            return nums[0]
        while i >= 0:
            if nums[i - 1] != nums[i]:
                return nums[i]
            else:
                t = i
                while t >= 0 and nums[t] == nums[i]:
                    t -= 1
                
                i = t + 1
            i -= 1
        return -1
            
                
        