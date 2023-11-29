class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n2 = []
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                n2.append(temp)
                temp = 0
                n2.append(0)
        else:
            n2.append(temp)
        print(n2, nums)
        ans = 0
        
        if len(n2) > 1:
            for i in range(2, len(n2)):
                ans = max(ans, n2[i] + n2[i-1] + n2[i-2] + 1)
        else:
            ans = sum(n2)
        return ans