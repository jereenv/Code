class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr = 0

        s = {0: -1}

        for i in range(len(nums)):
            curr = (curr + nums[i]) % k
            if curr in s:
                if i - s[curr] > 1:
                    return True
            else:
                s[curr] = i
        

        
        return False
            
        
        
            
        
            
            
            
        