class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for i in s:
            if i == t[idx]:
                idx += 1
            if idx == len(t):
                break
        return len(t) - idx
        