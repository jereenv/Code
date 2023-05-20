class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for ind, val in enumerate(nums):
            if target - val in dic:
                return [dic[target-val], ind]
            else:
                dic[val] = ind
        