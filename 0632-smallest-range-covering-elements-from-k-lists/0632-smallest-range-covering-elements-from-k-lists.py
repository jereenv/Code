class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        
        merged = []
        
        for i in range(k):
            for num in nums[i]:
                merged.append((num, i))
        
        merged.sort()
        
        freq = defaultdict(int)
        left, c = 0, 0
        
        s, e = 0, float("inf")
        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            
            if freq[merged[right][1]] == 1:
                c += 1
                
            
            while c == k:
                temp = merged[right][0] - merged[left][0]
                if temp < e - s:
                    s, e = merged[left][0], merged[right][0]
                
                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    c -= 1
                
                left += 1
            
            
        return [s, e]