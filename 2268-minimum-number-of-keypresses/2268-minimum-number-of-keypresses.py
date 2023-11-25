class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        ans = 0
        ctr = 1
        
        arr = []
        for i in freq:
            arr.append(freq[i])
        
        arr.sort(reverse = True)
        print(arr)
        
        for idx, val in enumerate(arr):
            ans += val * math.ceil((idx + 1)/9)
        return ans
            
        