class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for l in intervals:
            if ans and ans[-1][1] >= l[0]:
                ans[-1][1] = l[1] if l[1] > ans[-1][1] else ans[-1][1]
            else:
                ans.append(l)
        return ans
        