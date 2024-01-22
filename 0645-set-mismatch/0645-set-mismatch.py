class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        s = n * (n + 1)//2
        print(n, len(nums), nums, s)
        dic = defaultdict(bool)
        dup = -1
        for i in nums:
            if dic[i]:
                dup = i
            dic[i] = True
        print(s, sum(nums), dup)
        return [dup, s - sum(nums) + dup]
            
            
        
        
        