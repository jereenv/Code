class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n = len(nums)
        # def xor(a,b):
        #     ans = 
        #     for i in range(nums):
        #         if a[i] == b[i]:
        
        ans = nums[0]
        # nums = set(nums)
        
        for i in range(len(ans)):
            
            t = "1" if ans[i] == "0" else "0"
            temp = ans[:i] + t + ans[i+1:]
            if temp not in nums:
                return temp
                    
            
        