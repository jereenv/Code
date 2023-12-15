class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        
        
        for x,y in points:
            distances.append([(x)**2 + (y)**2,[x,y]])
        
        distances.sort()
        for idx in range(k):
            points[idx] = distances[idx][1]
        return points[:k]
        
        
        