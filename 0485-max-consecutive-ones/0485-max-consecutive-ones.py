class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for _ in nums:
            if _ == 1:
                temp +=1
            else:
                ans = max(ans, temp)
                temp = 0
        else:
            ans = max(ans, temp)
        return ans
        