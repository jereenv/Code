class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
        
        s1Count = [0]*26
        s2Count = [0]*26

        for i in range(len_s1):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        l = 0

        for i in range(len_s1,len_s2):
            if matches == 26:
                return True
            
            ind = ord(s2[i]) - ord("a")
            s2Count[ind] += 1
            if s2Count[ind] == s1Count[ind]:
                matches += 1
            elif s2Count[ind] - 1  == s1Count[ind]:
                matches -= 1
            
            ind = ord(s2[l]) - ord("a")
            s2Count[ind] -= 1
            if s2Count[ind] == s1Count[ind]:
                matches += 1
            elif s2Count[ind] + 1  == s1Count[ind]:
                matches -= 1
            
            l+=1
        return matches == 26
            