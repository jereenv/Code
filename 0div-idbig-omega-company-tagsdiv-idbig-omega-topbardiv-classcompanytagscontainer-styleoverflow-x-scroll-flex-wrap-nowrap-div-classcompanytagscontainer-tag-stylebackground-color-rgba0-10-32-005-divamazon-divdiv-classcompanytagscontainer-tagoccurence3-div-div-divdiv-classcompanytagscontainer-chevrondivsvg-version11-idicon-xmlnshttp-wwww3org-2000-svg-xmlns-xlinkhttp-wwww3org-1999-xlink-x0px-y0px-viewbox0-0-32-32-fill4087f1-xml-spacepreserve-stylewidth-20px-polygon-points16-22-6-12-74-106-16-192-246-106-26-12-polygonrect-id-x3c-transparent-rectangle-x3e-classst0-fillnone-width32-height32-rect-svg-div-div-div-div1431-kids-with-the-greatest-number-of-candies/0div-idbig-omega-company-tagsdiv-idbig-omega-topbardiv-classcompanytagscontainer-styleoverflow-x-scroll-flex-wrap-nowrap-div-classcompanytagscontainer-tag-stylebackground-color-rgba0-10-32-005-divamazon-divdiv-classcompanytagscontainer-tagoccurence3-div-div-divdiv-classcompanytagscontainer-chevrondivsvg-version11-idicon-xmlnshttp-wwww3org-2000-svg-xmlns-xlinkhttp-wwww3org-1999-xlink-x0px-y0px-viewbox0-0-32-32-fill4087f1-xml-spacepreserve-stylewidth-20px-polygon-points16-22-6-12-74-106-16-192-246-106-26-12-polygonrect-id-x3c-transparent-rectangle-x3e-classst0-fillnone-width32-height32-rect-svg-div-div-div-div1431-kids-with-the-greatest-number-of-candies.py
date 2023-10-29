class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies) - extraCandies
        return (c >= max_value for c in candies)
        