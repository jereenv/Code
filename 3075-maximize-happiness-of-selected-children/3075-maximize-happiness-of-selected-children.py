class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        ans = 0
        
        curr = 0
        
        happiness.sort()
        
        for _ in range(k):
            ans += max(happiness.pop() - curr, 0)
            
            curr += 1
        
        return ans