class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        idx = 0
        
        while idx < len(nums):
            if nums[idx] in s:
                nums.pop(idx)
            else:
                s.add(nums[idx])
                idx += 1
        