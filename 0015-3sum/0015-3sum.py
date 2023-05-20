class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        target = 0
        ans = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1
            while l < r:
                ThreeS = val + nums[l] + nums[r]
                if target < ThreeS:
                    r -= 1
                elif target > ThreeS:
                    l += 1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
                    
            
        