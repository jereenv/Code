class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        maxLen = 1
        i = 0
        j = 1
        print(nums)
        while j < len(nums):
            if nums[j] - 1 == nums[j-1]:
                pass
            else:
                print(i,j)
                maxLen = max(j-i, maxLen)
                i = j
            j += 1
        if len(nums) > 0:
            return max(j-i, maxLen)
        else:
            return 0