class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        c["1"] -= 1
        
        ans = "1" * c["1"] + "0"*c["0"] + "1"
        return ans
        