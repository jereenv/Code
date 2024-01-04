class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        idx = 0
        for word in words:
            if x in word:
                ans.append(idx)
            idx += 1
        return ans
        