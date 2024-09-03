class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def getNum(s):
            return str(ord(s) - ord('a') + 1)
        s = "".join([getNum(i) for i in s])
        
        def digSum(s):
            ans = 0
            for i in s:
                ans += int(i)
            return str(ans)
        
        while k:
            s = digSum(s)
            k -= 1
        return int(s)
        
        
        
        