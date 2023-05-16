class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for ind, val in enumerate(nums):
            nums[ind] = val ** 2
        return sorted(nums)
        