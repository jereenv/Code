class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 9999999
        end = -1
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                start = min(m, start)
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = start, len(nums) - 1
        
        if start == 9999999:
            return [-1, -1]
        
        while l <= r:
            m = (l + r)// 2
            if nums[m] == target:
                end = max(m, end)
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [start, end]
            
        
        