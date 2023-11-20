class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        
        travel = [0] + travel
        
        ans = 0
        for truck in ["P","M","G"]:
            travel_cost = 0
            for idx, g in enumerate(garbage):
                
                if truck in g:
                    ans += g.count(truck) + travel[idx] + travel_cost
                    travel_cost = 0
                else:
                    travel_cost += travel[idx]
        return ans
                    
                
        