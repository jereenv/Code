class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyPos = {}
        for i in range(len(keyboard)):
            keyPos[keyboard[i]] = i
        
        curr = 0
        ans = 0
        for i in word:
            ans += abs(keyPos[i] - curr)
            curr = keyPos[i]
        return ans
        