class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        def minMax(a):
            m1 = a[0]
            m2 = a[0]
            for i in a:
                m1 = min(m1, i)
                m2 = max(m2, i)
            
            return m1, m2
        
        m1 = []
        m2 = []
    
        
        for i in range(len(arrays)):
            m1.append([arrays[i][0], i])
            m2.append([arrays[i][-1], i])
        
        m1.sort()
        m2.sort()
        
        if m2[-1][1] != m1[0][1]:
            ans = m2[-1][0] - m1[0][0]
        else:
            ans = m2[-2][0] - m1[0][0] if m2[-2][0] - m1[0][0] > m2[-1][0] - m1[1][0] else m2[-1][0] - m1[1][0]
        return ans