class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1 = []
        f2 = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                f1 += [i]
                f2 += [n//i]
        
        if f1[-1] == f2[-1]:
            f2.pop()
        
        f1 = f1 + f2[::-1]
        
        return -1 if k > len(f1) else f1[k-1]