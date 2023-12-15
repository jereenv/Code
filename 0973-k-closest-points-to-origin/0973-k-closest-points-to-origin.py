class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for idx, val in enumerate(points):
            points[idx] =[(val[0])**2 + (val[1])**2,[val[0], val[1]]]
        
        points.sort()
        for idx in range(k):
            points[idx] = points[idx][1]
        return points[:k]
        
        
        