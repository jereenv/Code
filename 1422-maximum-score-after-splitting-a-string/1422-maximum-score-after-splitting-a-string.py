class Solution:
    def maxScore(self, s: str) -> int:
        
        score_left = 0
        score_right = s.count("1")
        ans = 0
        
        for i in range(len(s) - 1):
            if s[i] == "1":
                score_right -= 1
            else:
                score_left += 1
            ans = max(score_left + score_right, ans)
        return ans
        
       