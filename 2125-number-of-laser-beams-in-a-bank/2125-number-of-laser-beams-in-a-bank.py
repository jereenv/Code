class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        idx = 0
        while idx < len(bank):
            bank[idx] = bank[idx].count("1")
            idx += 1
        
        
        idx = 0
        ans = 0
        prev = 0
        while idx < len(bank) - 1:
            if bank[idx]:
                prev = bank[idx]
            ans += prev * bank[idx + 1]
            idx += 1
        return ans
            