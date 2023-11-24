class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        n = len(piles)
        idx = 1
        while idx < (n - n/3) :
            ans += piles[idx]
            idx += 2
        return ans
            
        
        