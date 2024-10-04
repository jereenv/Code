class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        ans = 0
        req = skill[0] + skill[-1]
        
        n = len(skill)
        
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != req:
                return -1
            ans += skill[i] * skill[n -1 - i]
        
        return ans