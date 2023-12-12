class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        one, two = -1, -1
        for num in nums:
            if num > one:
                two, one = one, num
            else:
                two = max(two, num)
        return (one - 1) * (two - 1)
        
        