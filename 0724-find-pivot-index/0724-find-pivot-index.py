class Solution:
    def pivotIndex(self, s: List[int]) -> int:

        Tsum = sum(s)

        Lsum = 0
        for i in range(len(s)):
            if Tsum - s[i] == Lsum:
                return i
            else:
                Tsum -= s[i]
                Lsum += s[i]
        return -1
