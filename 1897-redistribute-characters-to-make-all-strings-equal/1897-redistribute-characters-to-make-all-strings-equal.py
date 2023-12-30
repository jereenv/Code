class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for word in words:
            for i in word:
                dic[i] = 1 + dic.get(i,0)
        
        for i in dic:
            if dic[i]%len(words) != 0:
                return False
        return True
        