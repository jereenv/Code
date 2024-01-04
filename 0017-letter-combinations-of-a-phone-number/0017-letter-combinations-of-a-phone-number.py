class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        numkey = {
            "2":["a", "b", "c"], 
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
        
        n = len(digits)
        ans = []
        def dp(idx, arr):
            if len(arr) == n:
                ans.append("".join(arr))
                return
            
            for alpha in numkey[digits[idx]]:
                dp(idx + 1, arr + [alpha])
        
        dp(0, [])
        
        return ans
            
            
                
        