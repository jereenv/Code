class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        small = inf
        s_small = inf
        for i in prices:
            if i < small:
                s_small = small
                small = i
            else:
                s_small = min(i, s_small)
        ans = money - small - s_small
        return ans if ans >= 0 else money
        