class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        arr = [0]*26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        
        ans = 0
        arr.sort(reverse = True)
        
        for idx, val in enumerate(arr):
            ans += val * math.ceil((idx + 1)/9)
        return ans
            
        