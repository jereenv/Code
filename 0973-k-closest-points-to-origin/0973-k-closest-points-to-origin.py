class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for idx, val in enumerate(points):
            x,y = val
            points[idx] =[(x)**2 + (y)**2,[x,y]]
        
        points.sort()
        for idx in range(k):
            points[idx] = points[idx][1]
        return points[:k]
        
        
        