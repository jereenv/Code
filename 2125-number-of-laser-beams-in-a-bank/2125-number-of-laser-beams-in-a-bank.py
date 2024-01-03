class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        idx = 0
        while idx < len(bank):
            if int(bank[idx]) == 0:
                bank.pop(idx)
            else:
                count = 0
                for i in bank[idx]:
                    if i == "1":
                        count += 1
                bank[idx] = count
                idx += 1
        
        idx = 0
        ans = 0
        while idx < len(bank) - 1:
            ans += bank[idx] * bank[idx + 1]
            idx += 1
        return ans
            