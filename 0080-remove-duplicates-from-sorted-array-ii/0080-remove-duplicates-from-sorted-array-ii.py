class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        k = 1
        dic[nums[0]] += 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] or dic[nums[i]] < 2:
                nums[k] = nums[i]
                k += 1
            dic[nums[i]] += 1
        print(dic)
        return k