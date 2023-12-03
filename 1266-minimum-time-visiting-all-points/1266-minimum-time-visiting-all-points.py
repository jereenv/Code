class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x1,y1 = points.pop(0)
        time = 0
        
        for point in points:
            x2,y2 = point
            time += max(abs(x1 - x2), abs(y1 - y2))
            x1, y1 = x2, y2
        return time
            
                
            
                    
        