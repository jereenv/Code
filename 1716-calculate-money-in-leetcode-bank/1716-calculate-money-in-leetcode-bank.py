class Solution:
    def totalMoney(self, n: int) -> int:
        
        ans = 0
        s = 1
        while n > 0:
            for day in range(min(n, 7)):
                ans += s + day
            n -= 7
            s += 1
        return ans
        