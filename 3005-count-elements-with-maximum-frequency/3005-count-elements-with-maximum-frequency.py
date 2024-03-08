class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [[0, i] for i in range(1, 102)]
        for i in nums:
            freq[i][0] += 1
        
        freq.sort(reverse = True)
        
        ans = 0
        f = freq[0][0]
        
        for i in freq:
            if i[0] == f:
                ans += f
            else:
                break
        return ans
        