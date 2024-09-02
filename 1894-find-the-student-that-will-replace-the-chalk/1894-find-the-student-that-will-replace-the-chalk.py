class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k %= s
        
        idx = 0
        while k >= chalk[idx]:
            k -= chalk[idx]
            idx += 1
        
        return idx
        