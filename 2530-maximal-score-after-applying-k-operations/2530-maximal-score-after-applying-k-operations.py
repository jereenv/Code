class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        nums = [-x for x in nums]
        ans = 0
        heapq.heapify(nums)
        
        while k:
 
            num = heapq.heappop(nums)
            ans -= num
            heapq.heappush(nums, math.floor(num/3))
            
            k -= 1
        
        return ans
