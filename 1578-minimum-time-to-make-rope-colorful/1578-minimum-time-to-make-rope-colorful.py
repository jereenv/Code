class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        
        idx = 0
        while idx < len(colors) - 1:
            if colors[idx] == colors[idx + 1]:
                tc = 0
                i = 0
                m = 0
                while idx + i < len(colors) and colors[idx] == colors[idx + i]:
                    tc += neededTime[idx + i]
                    m = max(m, neededTime[idx + i])
                    i += 1
                cost += tc - m
                idx += i - 1
            idx += 1
        return cost
            