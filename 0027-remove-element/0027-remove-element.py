class Solution:
    def removeElement(self, nums: List[int], v: int) -> int:
        k = 0
        
        for idx, val in enumerate(nums):
            if v != val:
                nums[k] = val
                k += 1
        return k
        