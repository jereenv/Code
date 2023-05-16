class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic = {}
        s1 = set()
        for i, val in enumerate(s):
            if t[i] in dic:
                if dic[t[i]] != val:
                    return False
            else:
                # This means that a pair has already been established for that character
                if val in s1:
                    return False
                dic[t[i]] = val
                s1.add(val)
        return True