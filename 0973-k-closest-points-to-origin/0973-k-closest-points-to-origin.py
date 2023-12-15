class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        def getEuclidean(x1,y1):
            return (x1)**2 + (y1)**2
        
        for x,y in points:
            distances.append([getEuclidean(x,y),[x,y]])
        
        distances.sort()
        ans = []
        for idx in range(k):
            ans.append(distances[idx][1])
        return ans
        
        
        