class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        #Total path = Dis(nut1, s) + Dis(tree, nut1) + 2 * (Dis(nut2, tree) + .... + Dis(nutn, tree))
        
        #  = Dis(all nuts, tree) * 2  - Dis(Optimal Nut, tree) + Dis(Optimal Nut, Squirrel)
        
        # Therefore, max(Dis(Optimal Nut, tree) - Dis(Optimal Nut, Squirrel)) is required
        
        
        def distance(ob1, ob2):
            return abs(ob1[0] - ob2[0]) + abs(ob1[1] - ob2[1])
        
        f_dis = -99999
        total_dis = 0
        
        for nut in nuts:
            f_dis = max(f_dis, distance(nut, tree) - distance(nut, squirrel))
            total_dis += distance(nut, tree)
        
        
        return 2*total_dis - f_dis
        