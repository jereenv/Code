class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []
        for i in candies:
             ans.append(i + extraCandies >= m)
        return ans
        