class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        monsters = [[monster, coin] for monster, coin in zip(monsters, coins)]
        
        monsters.sort()
        
        
        ans = []
        
        curr_idx = 0
        n = len(monsters)
        
        s_heroes = sorted(heroes)
        
        for idx, power in enumerate(s_heroes):
            
            reward = 0 if idx == 0 else ans[-1]
            while curr_idx < n:
                if monsters[curr_idx][0] > power:
                    break
                reward += monsters[curr_idx][1]
                curr_idx += 1
            
                
                
                
            ans.append(reward)
        
        freq = {s_heroes[i]: ans[i] for i in range(len(heroes))}
        
        return [freq[i] for i in heroes]
        