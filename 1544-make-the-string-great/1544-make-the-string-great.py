class Solution:
    def makeGood(self, w: str) -> str:
        s = deque()
        s.append(w[0])
        n = len(w)
        i = 1
        while i < len(w):
            if s and abs(ord(s[-1]) - ord(w[i])) == 32:
                s.pop()
            else:
                s.append(w[i])
            i += 1
        
        return "".join(s)
        