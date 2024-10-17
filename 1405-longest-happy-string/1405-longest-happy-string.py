class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        curra, currb, currc = 0, 0, 0
        
        total_iterations = a + b + c
        
        result = []
        
        for _ in range(total_iterations):
            if ((a >= b and a >= c and curra < 2) or (a > 0 and (currb == 2 or currc == 2))):
                result.append("a")
                curra += 1
                a -= 1
                currb = 0
                currc = 0
            elif ((b >= a and b >= c and currb < 2) or (b > 0 and (curra == 2 or currc == 2))):
                result.append("b")
                currb += 1
                b -= 1
                curra = 0
                currc = 0
            elif ((c >= a and c >= b and currc < 2) or (c > 0 and (curra == 2 or currb == 2))):
                result.append("c")
                currc += 1
                c -= 1
                currb = 0
                curra = 0
        
        return "".join(result)