class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mLen = 0
        nums = set(nums)
        
        for i in nums:
            if i-1 not in nums:
                temp = 0
                while i + temp in nums:
                    temp += 1
                mLen = max(mLen, temp)
        return mLen