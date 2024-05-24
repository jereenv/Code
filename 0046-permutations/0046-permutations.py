class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        res = []
        
        if n == 1:
            return [nums[:]]
        
        for _ in range(n):
            last = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(last)
            
            res.extend(perms)
            nums.append(last)
        return res