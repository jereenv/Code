class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        
        freq = Counter(s)
        
        for i in order:
            ans += i*freq[i]
            freq[i] = 0
        
        for i in freq:
            if freq[i] > 0:
                ans += i*freq[i]
        
        return ans