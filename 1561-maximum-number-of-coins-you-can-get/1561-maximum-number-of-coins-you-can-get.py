class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        alice = 0
        us = 0
        bob = 0
        
        while queue:
            alice = queue.pop()
            us += queue.pop()
            bob = queue.popleft()
            
        return us
            
        
        