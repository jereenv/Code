class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for key in counter:
            if counter[key] == 1:
                return -1
            ans += ceil(counter[key]/3)
        return ans
        