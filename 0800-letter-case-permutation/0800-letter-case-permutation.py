class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def permutation(s1, i):
            if i < len(s):
                if s[i].isalpha():
                    permutation(s1 + s[i].lower(), i + 1)
                    permutation(s1 + s[i].upper(), i + 1)
                else:
                    permutation(s1 + s[i].upper(), i + 1)
            else:
                ans.append(s1)
        
        permutation("",0)
        return ans
            