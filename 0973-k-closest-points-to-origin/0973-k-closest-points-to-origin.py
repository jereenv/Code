class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        
        
        for x,y in points:
            distances.append([(x)**2 + (y)**2,[x,y]])
        
        distances.sort()
        ans = []
        for idx in range(k):
            ans.append(distances[idx][1])
        return ans
        
        
        