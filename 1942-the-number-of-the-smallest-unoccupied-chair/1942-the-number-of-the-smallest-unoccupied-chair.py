class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        times = [(s, e, idx) for idx, (s, e) in enumerate(times)]
        
        times.sort()
        
        used_chair = []
        available_chairs = [i for i in range(len(times))]
        
        for s, e, idx in times:
            
            while used_chair and used_chair[0][0] <= s:
                leave, chair = heapq.heappop(used_chair)
                heapq.heappush(available_chairs, chair)
            
            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chair, (e, chair))
            
            if idx == targetFriend:
                return chair
                
            
        
        
        