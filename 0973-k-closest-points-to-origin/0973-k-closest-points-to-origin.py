from heapq import heappop, heappush, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pd = defaultdict(list)
        d = []
        for x, y in points:
            dis = (x**2 + y**2)**0.5
            d.append(dis)
            pd[dis].append([x, y])
        
        heapify(d)
        ans = []
        
        while k:
            t = pd[heappop(d)]
            ans.extend(t)
            k -= len(t)
        return ans
        
        
        
        