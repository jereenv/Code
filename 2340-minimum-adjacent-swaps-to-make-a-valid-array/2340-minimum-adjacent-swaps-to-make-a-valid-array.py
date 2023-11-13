class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        l = len(nums)
        count = 0
        m1 = min(nums)
        m2 = max(nums)
        
        m1_pos = l - 1
        m2_pos = 0
        
        for i in range(l):
            if nums[i] == m2:
                m2_pos = max(i, m2_pos)
            if nums[i] == m1:
                m1_pos = min(i, m1_pos)
        
        if m2_pos < m1_pos:
            for i in range(m2_pos, l - 1):
                nums[i], nums[i+ 1] = nums[i +1], nums[i]
                count += 1
        else:
            count = l - 1 - m2_pos
        for i in range(l):
            if nums[i] == m2:
                m2_pos = max(i, m2_pos)
            if nums[i] == m1:
                m1_pos = min(i, m1_pos)
        
        print(m1_pos, m2_pos)

        return count + m1_pos
        