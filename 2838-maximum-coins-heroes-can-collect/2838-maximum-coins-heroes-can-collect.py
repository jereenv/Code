class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        monsters = sorted(zip(monsters, coins))
        
        s_heroes = sorted((power, idx) for idx, power in enumerate(heroes))
        n = len(monsters)
        
        ans = [0] * len(heroes) 
        curr_idx, reward = 0, 0  
        
        for power, original_idx in s_heroes:
            while curr_idx < n and monsters[curr_idx][0] <= power:
                reward += monsters[curr_idx][1]
                curr_idx += 1
            ans[original_idx] = reward
        
        return ans
        