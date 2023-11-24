class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for idx in range(len(l)):
            temp = sorted(nums[l[idx]:r[idx] + 1])
            #print(temp)
            for i in range(1,r[idx]-l[idx]):
                #print(temp[i] - temp[i-1], temp[i+1] - temp[i], i, temp)
                if temp[i] - temp[i-1] != temp[i+1] - temp[i]:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans
                    
                
                
                
        