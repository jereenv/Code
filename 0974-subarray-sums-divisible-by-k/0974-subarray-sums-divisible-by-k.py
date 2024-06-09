class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        dic = {0:1}
        
        n = len(nums)
        
        curr = 0
        
        ans = 0
        
        for i in range(n):
            curr = (curr + nums[i])%k
            
            if curr in dic:
                ans += dic[curr]
            dic[curr] = 1 + dic.get(curr, 0)
        
        return ans