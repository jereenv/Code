class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:       
        c = Counter(arr)
        for i in arr:
            if c[i] == 1:
                k -= 1
            
            if not k:
                return i
        return ""