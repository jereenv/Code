class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        gcd = lambda a,b : a if b == 0 else gcd(b, a % b)
        
        k = gcd(len(str1), len(str2))
        
        return str1[:k]
            
        