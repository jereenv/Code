class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        arr = [0]*26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        
#         print(freq1)
        
#         freq = {}
#         for i in s:
#             if i not in freq:
#                 freq[i] = 0
#             freq[i] += 1

#         arr = []
        # for i in freq:
        #     arr.append(freq[i])
        
        ans = 0
        arr.sort(reverse = True)
        
        for idx, val in enumerate(arr):
            ans += val * math.ceil((idx + 1)/9)
        return ans
            
        