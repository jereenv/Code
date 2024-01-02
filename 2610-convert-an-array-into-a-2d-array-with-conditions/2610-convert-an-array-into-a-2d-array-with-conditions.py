class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in nums:
            idx = 0
            while True:
                if idx >= len(ans):
                    ans.append(set())
                else:
                    if i not in ans[idx]:
                        ans[idx].add(i)
                        break
                    else:
                        idx += 1
        for idx in range(len(ans)):
            ans[idx] = list(ans[idx])
            
        return ans
        
        