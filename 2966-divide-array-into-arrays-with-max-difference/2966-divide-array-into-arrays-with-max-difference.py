class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        nums = [nums[i:i + 3] for i in range(0, len(nums), 3)]
        
        for x, y, z in nums:
            if z - x > k:
                return []
        return nums
        
        