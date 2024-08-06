import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        char_freq = Counter(word)
               
        freq_arr = [(char_freq[char], char) for char in char_freq]
        
        freq_arr.sort(reverse = True)
   
        k = 8
        ans = 0
        for idx, val in enumerate(freq_arr):
            freq, char = val
            ans += ((idx // k) + 1) * freq
        return ans