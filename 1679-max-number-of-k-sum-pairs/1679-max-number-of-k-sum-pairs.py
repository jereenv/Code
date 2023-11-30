class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dic = {}
#         for i in nums:
#             num_dic[i] = 1 + num_dic.get(i, 0)
        
#         ans = 0
#         for i in num_dic:
#             if k - i in num_dic and num_dic[k-i] > 0:
                
#                 if k - i != i:
#                     ans += min(num_dic[k-i], num_dic[i])
#                     num_dic[k-i] -= num_dic[i]
#                     num_dic[i] = 0
#                 else:
#                     ans += num_dic[i]//2
#         return ans

        ans = 0
        for num in nums:
            if k - num in num_dic and num_dic[k - num] > 0:
                ans += 1
                num_dic[k - num] -= 1
            else:
                num_dic[num] = 1 + num_dic.get(num, 0)
        return ans
        
        
        
        
        
            
        
        