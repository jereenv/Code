class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = float('inf')
        end = -1
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] >= target:
                if nums[m] == target:
                    start = min(m, start)
                r = m - 1
            else:
                l = m + 1
        
        l, r = start, len(nums) - 1
        
        if start == float('inf'):
            return [-1, -1]
        
        while l <= r:
            m = (l + r)// 2
            if nums[m] > target:
                r = m - 1
            else:
                if nums[m] == target:
                    end = max(m, end)
                l = m + 1
        return [start, end]
            
        
        