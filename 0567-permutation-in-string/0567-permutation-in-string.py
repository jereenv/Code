class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        if len(s1) > len(s2):
            return False
        
        s1Dic = {}
        s2Dic = {}
        
        for i in s1:
            s1Dic[i] = 1 + s1Dic.get(i,0)

        l = 0
        
        for i in range(len(s1)):
            s2Dic[s2[i]] = 1 + s2Dic.get(s2[i], 0)

        if s1Dic == s2Dic:
            return True
        
        for r in range(len(s1), len(s2)):
            if s1Dic == s2Dic:
                return True
            
            s2Dic[s2[l]] -= 1
            s2Dic[s2[r]] =  1 + s2Dic.get(s2[r], 0)
            if s2Dic[s2[l]] <= 0:
                s2Dic.pop(s2[l])
            l +=1
        
        return s1Dic == s2Dic
        
            
#         len_s1 = len(s1)
#         len_s2 = len(s2)

#         if len_s1 > len_s2:
#             return False
        
#         s1Count = [0]*26
#         s2Count = [0]*26

#         for i in range(len_s1):
#             s1Count[ord(s1[i]) - ord("a")] += 1
#             s2Count[ord(s2[i]) - ord("a")] += 1
        
#         matches = 0
#         for i in range(26):
#             matches += 1 if s1Count[i] == s2Count[i] else 0
        
#         l = 0

#         for i in range(len_s1,len_s2):
#             if matches == 26:
#                 return True
            
#             ind = ord(s2[i]) - ord("a")
#             s2Count[ind] += 1
#             if s2Count[ind] == s1Count[ind]:
#                 matches += 1
#             elif s2Count[ind] - 1  == s1Count[ind]:
#                 matches -= 1
            
#             ind = ord(s2[l]) - ord("a")
#             s2Count[ind] -= 1
#             if s2Count[ind] == s1Count[ind]:
#                 matches += 1
#             elif s2Count[ind] + 1  == s1Count[ind]:
#                 matches -= 1
            
#             l+=1
#         return matches == 26
