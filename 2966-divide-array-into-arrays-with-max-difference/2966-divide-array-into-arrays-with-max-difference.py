class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        ans = [nums[i:i + 3] for i in range(0, len(nums), 3)]
        
        for arr in ans:
            if abs(arr[0] - arr[1]) > k or abs(arr[1] - arr[2]) > k or abs(arr[2] - arr[0]) > k:
                return []
        return ans
            
        
        