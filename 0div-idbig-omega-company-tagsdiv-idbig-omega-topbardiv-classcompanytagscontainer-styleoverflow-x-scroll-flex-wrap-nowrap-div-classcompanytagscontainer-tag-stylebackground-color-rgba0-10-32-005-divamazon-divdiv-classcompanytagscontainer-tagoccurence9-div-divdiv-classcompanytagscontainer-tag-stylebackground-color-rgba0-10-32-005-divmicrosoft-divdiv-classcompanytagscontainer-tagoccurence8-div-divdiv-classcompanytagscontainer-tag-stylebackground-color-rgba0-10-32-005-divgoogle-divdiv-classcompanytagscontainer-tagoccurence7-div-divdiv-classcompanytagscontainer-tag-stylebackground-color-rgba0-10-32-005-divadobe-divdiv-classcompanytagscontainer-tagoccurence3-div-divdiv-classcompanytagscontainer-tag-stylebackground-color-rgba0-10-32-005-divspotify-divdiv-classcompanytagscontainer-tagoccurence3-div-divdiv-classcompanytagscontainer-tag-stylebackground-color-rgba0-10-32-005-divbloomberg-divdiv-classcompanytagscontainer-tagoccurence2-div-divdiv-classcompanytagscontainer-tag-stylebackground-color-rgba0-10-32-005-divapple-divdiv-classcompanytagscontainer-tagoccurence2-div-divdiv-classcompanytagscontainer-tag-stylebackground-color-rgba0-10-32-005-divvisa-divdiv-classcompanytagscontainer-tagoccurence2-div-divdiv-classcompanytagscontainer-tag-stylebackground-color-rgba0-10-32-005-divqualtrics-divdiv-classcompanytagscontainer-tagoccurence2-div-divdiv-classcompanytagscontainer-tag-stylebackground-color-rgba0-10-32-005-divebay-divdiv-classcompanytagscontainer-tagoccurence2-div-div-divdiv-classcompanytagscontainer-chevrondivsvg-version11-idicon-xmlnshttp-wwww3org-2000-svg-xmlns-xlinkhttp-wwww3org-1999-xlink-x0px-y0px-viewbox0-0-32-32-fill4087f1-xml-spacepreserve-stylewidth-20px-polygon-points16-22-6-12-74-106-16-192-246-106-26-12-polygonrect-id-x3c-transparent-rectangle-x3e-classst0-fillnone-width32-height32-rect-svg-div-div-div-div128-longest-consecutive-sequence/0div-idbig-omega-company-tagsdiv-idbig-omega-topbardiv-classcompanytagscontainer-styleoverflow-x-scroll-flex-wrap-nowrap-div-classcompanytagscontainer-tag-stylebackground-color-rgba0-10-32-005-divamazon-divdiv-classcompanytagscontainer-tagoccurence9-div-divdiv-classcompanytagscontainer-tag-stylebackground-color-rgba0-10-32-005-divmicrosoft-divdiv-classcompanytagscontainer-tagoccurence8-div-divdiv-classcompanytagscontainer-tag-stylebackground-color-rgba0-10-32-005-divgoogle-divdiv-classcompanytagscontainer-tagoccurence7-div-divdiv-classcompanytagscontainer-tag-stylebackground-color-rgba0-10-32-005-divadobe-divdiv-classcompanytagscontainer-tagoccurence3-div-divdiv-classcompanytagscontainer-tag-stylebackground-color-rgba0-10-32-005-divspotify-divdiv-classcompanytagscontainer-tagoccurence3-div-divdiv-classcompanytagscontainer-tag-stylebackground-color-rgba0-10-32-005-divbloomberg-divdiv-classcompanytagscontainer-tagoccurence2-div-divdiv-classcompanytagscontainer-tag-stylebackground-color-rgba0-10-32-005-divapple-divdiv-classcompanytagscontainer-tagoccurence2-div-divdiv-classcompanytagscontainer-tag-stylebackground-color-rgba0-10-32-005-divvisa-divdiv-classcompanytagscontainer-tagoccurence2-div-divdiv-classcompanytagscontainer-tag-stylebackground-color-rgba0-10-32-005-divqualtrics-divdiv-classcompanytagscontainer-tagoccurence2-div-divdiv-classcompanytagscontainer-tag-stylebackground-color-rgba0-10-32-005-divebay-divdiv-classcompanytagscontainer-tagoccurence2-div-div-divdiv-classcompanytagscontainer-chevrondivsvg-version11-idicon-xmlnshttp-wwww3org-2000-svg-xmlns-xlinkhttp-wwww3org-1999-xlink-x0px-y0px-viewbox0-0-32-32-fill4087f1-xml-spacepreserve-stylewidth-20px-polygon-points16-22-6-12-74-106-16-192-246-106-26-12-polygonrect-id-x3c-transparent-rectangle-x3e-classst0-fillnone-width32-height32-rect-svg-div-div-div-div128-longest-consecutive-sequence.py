class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ls = 0
        
        nums = set(nums)
        
        
        for curr in nums:
            
            if curr - 1 not in nums:
                l = 1
                
                while curr + 1 in nums:
                    l += 1
                    curr += 1
                
                ls = max(l, ls)
        return ls
            
            
        