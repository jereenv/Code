class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop(-2)
                stones.pop(-1)
            elif stones[-1] > stones[-2]:
                stones[-1] -= stones[-2]
                stones.pop(-2)
            else:
                stones[-2] -= stones[-1]
                stones.pop(-1)
        if len(stones):
            return stones[0]
        return 0
        
        