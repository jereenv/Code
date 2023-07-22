class Solution:
    def reverse(self, x: int) -> int:
        m1 =  2**31 - 1
        m2 = (m1 + 1) * (-1)
        lenM = len(str(m1))
        
        sX = str(abs(x))
        if len(sX) < lenM:
            return int(str(sX)[::-1]) * (-1) if x < 0 else int(str(sX)[::-1])
        else:
            if x < 0:
                iX = int(str(sX)[::-1]) * (-1)
                if iX >= m2:
                    return iX
            else:
                iX = int(str(sX)[::-1])
                if iX <= m1:
                    return iX
        return 0
            
        