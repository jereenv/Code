class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l,r = 0, k
        
        count = {}
        
        m = 0
        
        currSum = 0
        for i in nums[:k]:
            if i not in count:
                count[i] = 0
            count[i] += 1
            currSum += i
        
        if len(count) == k:
            m = currSum
            
        

        while r < len(nums):

            count[nums[r]] = 1 + count.get(nums[r], 0)
            count[nums[l]] -= 1
            if count[nums[l]] == 0:
                count.pop(nums[l])
            currSum += nums[r] - nums[l]
            r += 1
            l += 1
            if len(count) == k:
                m = max(m, currSum)
        
        return m
                    
                    