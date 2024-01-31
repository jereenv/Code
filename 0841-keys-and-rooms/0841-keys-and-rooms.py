class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        vis = set()
        keys = set()
        
        def dfs(room):
            if room in vis:
                return
            vis.add(room)
            
            for key in rooms[room]:
                dfs(key)
        vis.add(0)
        for room in rooms[0]:
            dfs(room)
        
        return len(vis) == len(rooms)
            
            
        