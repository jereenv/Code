class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        
        dp = [[x, y] for x, y in zip(difficulty, profit)]
        
        n = [len(dp)]
        
        dp.sort()
        
        curr = 0
        
        for idx, val in enumerate(dp):
            curr = max(curr, val[1])
            dp[idx][1] = curr
        
        
        print(dp)
        print(worker)
        
        
        def binarySearch(w):
            l, r = 0, n[0] - 1
            
            while l <= r:
                m = (l + r)//2
                if dp[m][0] > w:
                    r = m - 1
                elif dp[m][0] == w:
                    if m < n[0] - 1 and dp[m + 1][0] == w:
                        l = m + 1
                    else:
                        return dp[m][1]
                        
                else:
                    l = m + 1
            return dp[r][1] if dp[r][0] <= w else 0
        
        p = 0
        for w in worker:
            
            
            curr = binarySearch(w)
            #print(w, curr)
            p += curr
        
        return p