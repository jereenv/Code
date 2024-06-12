class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        n = [0]*3
        
        for i in nums:
            n[i] += 1
        
        idx = 0
        print(n)
        for i, val in enumerate(n):
            for _ in range(val):
                nums[idx] = i
                idx += 1