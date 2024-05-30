class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        count = 0
        xor_count = {}
        
        for k in range(n):
            for j in range(k + 1, n):
                if prefix_xor[k] == prefix_xor[j + 1]:
                    count += (j - k)
                    
        return count