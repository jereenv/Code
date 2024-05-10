class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        
        for i in arr:
            for j in arr:
                if i != j:
                    fractions.append([i/j, i, j])
        
        fractions.sort()
        
        
        return fractions[k-1][1], fractions[k-1][2]