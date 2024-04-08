class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True  # Starting position is reachable

        for i in range(n):
            if reachable[i]:
                # Explore all reachable distances from current index
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    reachable[j] = True

        return reachable[n - 1]  # Check if last position is reachable
