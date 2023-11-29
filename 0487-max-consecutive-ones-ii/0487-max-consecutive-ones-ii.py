class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ans = 0
        l, r = 0, 0
        zeros = 0
        
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            while zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        return ans