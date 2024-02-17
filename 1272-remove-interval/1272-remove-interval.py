class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        ans = []
        start, end = toBeRemoved
        for [s1, e1] in intervals:
            
            if e1 <= start:
                ans.append([s1, e1])
            elif start < e1 <= end:
                if s1 < start:
                    ans.append([s1, start])
            elif s1 >= end:
                ans.append([s1, e1])
            else:
                if s1 < start:
                    ans.append([s1, start])
                ans.append([end, e1])

        
        return ans