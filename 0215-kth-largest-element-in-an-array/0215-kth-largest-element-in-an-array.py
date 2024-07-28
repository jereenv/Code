from heapq import heappop, heappush, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        
        heapify(nums)
        
        k-= 1
        
        while k:
            heappop(nums)
            k-= 1
        
        return -heappop(nums)
        
        