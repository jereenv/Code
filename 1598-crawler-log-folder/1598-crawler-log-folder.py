class Solution:
    def minOperations(self, logs: List[str]) -> int:
        remain = "./"
        parent = "../"
        
        ans = 0
        for l in logs:
            if l == parent:
                if ans > 0:
                    ans -= 1
            elif l != remain:
                ans += 1
        
        return abs(ans)
            
        