class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = [0 for _ in range(len(nums))]
        l = 0
        r = len(nums) - 1
        i = r
        while i >= 0:
            s1 = nums[l] ** 2
            s2 = nums[r] ** 2
            if s1 > s2:
                ans[i] = s1
                l += 1
            else:
                ans[i] = s2
                r -= 1
            i -= 1
        return ans
                
        