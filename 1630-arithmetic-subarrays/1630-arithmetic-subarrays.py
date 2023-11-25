class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(nums):
            

            start = min(nums)
            end = max(nums)

            diff = (end - start)/(len(nums) - 1)

            if diff != int(diff):
                return False
            nums = set(nums)
            curr = start + diff
            while curr < end:
                if curr not in nums:
                    return False
                curr += diff
            return True
        
        
        ans = []
        for idx in range(len(l)):
            ans.append(check(nums[l[idx]: r[idx] + 1]))
        return ans