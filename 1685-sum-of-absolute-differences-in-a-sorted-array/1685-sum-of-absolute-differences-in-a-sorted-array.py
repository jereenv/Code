class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        rsum = sum(nums)
        lsum = 0
        
        for idx in range(n):
            temp1 = rsum - (n - idx)*nums[idx]
            temp2 = idx*nums[idx] - lsum
            
            rsum -= nums[idx]
            lsum += nums[idx]
            
            ans.append(temp1 + temp2)

        
        return ans
        