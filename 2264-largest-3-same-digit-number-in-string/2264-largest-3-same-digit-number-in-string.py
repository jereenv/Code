class Solution:
    def largestGoodInteger(self, num: str) -> str:
        idx = 0
        ans = -1
        while idx < len(num) - 2:
            if num[idx] == num[idx + 1] == num[idx+2]:
                ans = max(ans, int(num[idx] + num[idx + 1] + num[idx + 2]))
                idx += 2
            idx += 1
        if ans == -1:
            return ""
        if ans == 0:
            return "000"
        return str(ans)