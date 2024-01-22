class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        s = n * (n + 1)//2
        dic = defaultdict(bool)
        dup = -1
        for i in nums:
            if dic[i]:
                dup = i
                break
            dic[i] = True
        return [dup, s - sum(nums) + dup]
            
            
        
        
        