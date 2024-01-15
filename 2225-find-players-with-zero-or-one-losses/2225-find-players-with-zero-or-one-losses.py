class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lf = {}
        for w,l in matches:
            if w not in lf:
                lf[w] = 0
            
            if l not in lf:
                lf[l] = 0
            lf[l] += 1
        
        z = []
        o = []
        for i in lf:
            if lf[i] == 0:
                z.append(i)
            if lf[i] == 1:
                o.append(i)
        
        return [sorted(z), sorted(o)]