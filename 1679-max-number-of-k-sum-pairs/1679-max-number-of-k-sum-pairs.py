class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dic = {}
        ans = 0
        for num in nums:
            if k - num in num_dic and num_dic[k - num] > 0:
                ans += 1
                num_dic[k - num] -= 1
            else:
                num_dic[num] = 1 + num_dic.get(num, 0)
        return ans
        
        
        
        
        
            
        
        