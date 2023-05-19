class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        k = 0
        ans = 0
        s = list(s)
        while k < len(s):
            if s[k] == " ":
                r = k - 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = k + 1
            k += 1
        if l < k - 1:
            r = k - 1
            while l < r :
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l = k + 1
        return "".join(s)
            