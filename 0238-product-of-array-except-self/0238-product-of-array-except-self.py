class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        numZeros = 0
        ans = [0] * len(nums)
        
        for i in nums:
            if i == 0:
                numZeros += 1
        if numZeros > 1:
            return ans
        elif numZeros == 1:
            p = 1
            ind = 0
            for inde, i in enumerate(nums):
                if i != 0:
                    p *= i
                else:
                    ind = inde
            ans[ind] = p
        else:
            p = 1
            for inde, i in enumerate(nums):
                p *= i
            for i, val in enumerate(nums):
                ans[i] = p//val
        return ans
            