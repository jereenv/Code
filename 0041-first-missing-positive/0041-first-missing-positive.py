class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        seen = [False] * (n)
        
        for num in nums:
            if n >= num > 0:
                seen[num - 1] = True
        
        for idx, val in enumerate(seen):
            if not val:
                return idx + 1
        
        return n + 1
        