class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        idx = 0
        ans = 0
        k = 0
        while idx < len(nums):
            if nums[idx] == 0:
                k += 1
                temp = 1
                for l in range(idx - 1, -1, -1):
                    if nums[l] != 1:
                        break
                    temp += 1
                for r in range(idx + 1, len(nums), 1):
                    if nums[r] != 1:
                        break
                    temp += 1
                ans = max(ans, temp)
            idx += 1
        
        if k == 0:
            return len(nums)
        return ans
        