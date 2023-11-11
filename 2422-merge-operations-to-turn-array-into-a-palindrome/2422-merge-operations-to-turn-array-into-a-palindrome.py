class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        op = 0
        while l < r:
            if nums[l] < nums[r]:
                temp = nums.pop(l) + nums[l]
                nums[l] = temp
                op += 1
                r -= 1
            elif nums[l] > nums[r] and r - 1 > l:
                temp = nums.pop(r) + nums[r - 1]
                nums[r - 1] = temp
                r = r - 1
                op += 1
            else:
                l += 1
                r -= 1
            

        
        if nums[l] != nums[r]:
            op += 1
        return op