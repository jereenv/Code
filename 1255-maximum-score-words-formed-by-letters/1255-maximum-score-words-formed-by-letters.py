class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        n = len(words)
        
        letter_dic = defaultdict(int)
        for i in letters:
            letter_dic[i] += 1
        
        
        def backtrack(idx, total, letter_dic):
            if idx == n:
                return total
            
            without_score = backtrack(idx + 1, total, letter_dic.copy())
            
            a, b = self.calculateScore(words[idx], score, letter_dic.copy(), total)
            with_score = backtrack(idx + 1,a, b )
            
            return max(with_score, without_score)
        
        return backtrack(0,0,letter_dic)
    
    
    def calculateScore(self, word, scores, letter_dic, score):
        
        curr_sum = 0
        for w in word:
            if letter_dic[w] <= 0:
                return -float('inf'), letter_dic
                
            curr_sum += scores[ord(w) - ord('a')]
            letter_dic[w] -= 1
            
        return score + curr_sum, letter_dic