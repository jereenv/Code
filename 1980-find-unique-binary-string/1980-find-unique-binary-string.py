class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n = len(nums)
        # def xor(a,b):
        #     ans = 
        #     for i in range(nums):
        #         if a[i] == b[i]:
        
        nums = set(nums)
        n = len(nums)
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""
            
            t = generate(curr + "0")
            if t:
                return t
            return generate(curr + "1")
        
        return generate("")
                    
            
        