class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        
        ans = 0
        
        for word in words:
            ans += len(word)
            word_freq = Counter(word)
            for char in word_freq:
                if word_freq[char] > freq[char]:
                    ans -= len(word)
                    break
        return ans