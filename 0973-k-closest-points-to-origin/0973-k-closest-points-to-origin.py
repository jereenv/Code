class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        def getEuclidean(x1,x2,y1,y2):
            return ((x1-x2)**2 + (y1-y2)**2)
        
        for x,y in points:
            distances.append([getEuclidean(0,x,0,y),[x,y]])
        
        distances.sort()
        ans = []
        for idx in range(k):
            ans.append(distances[idx][1])
        return ans
        
        
        