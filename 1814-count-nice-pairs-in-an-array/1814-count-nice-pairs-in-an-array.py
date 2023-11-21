class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(num):
            digit = 0
            ans = 0
            while num > 0:
                ans = ans * 10 + num%10
                num //=10
            return ans
        print(nums)
        for idx, val in enumerate(nums):
            nums[idx] = val - rev(val)
        print(nums)
        
        freq = {}
        count = 0
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            count += freq[num]
            freq[num] += 1
        return count%(10**9 + 7)
        
            