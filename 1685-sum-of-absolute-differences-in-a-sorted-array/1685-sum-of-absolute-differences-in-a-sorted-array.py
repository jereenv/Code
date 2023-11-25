class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        rsum = sum(nums)
        lsum = 0
        
        for idx in range(n):
            ans.append(rsum - (n - idx)*nums[idx] + idx*nums[idx] - lsum)
            rsum -= nums[idx]
            lsum += nums[idx]
        return ans
        