class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        c1 = Counter(word1)
        c1_freq = {}
        
        for i in c1:
            if c1[i] not in c1_freq:
                c1_freq[c1[i]] = 0
            c1_freq[c1[i]] += 1
        
        c2 = Counter(word2)
        c2_freq = {}
        for i in c2:
            if c2[i] not in c2_freq:
                c2_freq[c2[i]] = 0
            c2_freq[c2[i]] += 1
        
        for i in c2_freq:
            if i not in c1_freq or c1_freq[i] != c2_freq[i]:
                return False
        return True
        
        
        