class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_str = list(str(num))
        n = len(num_str)
        
        curr_max = n - 1
        
        s1, s2 = -1, -1
        
        for i in range(n - 2, -1 , -1):
            if num_str[i] > num_str[curr_max]:
                curr_max = i
            
            elif num_str[i] < num_str[curr_max]:
                s1, s2 = i, curr_max
        
        num_str[s1], num_str[s2] = num_str[s2], num_str[s1]
        
        return int("".join(num_str))
        
        
#         optimal = [(int(val), idx) for idx, val in enumerate(num_str)]
#         optimal.sort(reverse = True, key = lambda x: (x[0], -x[1]))
#         #print(optimal)
        
        
#         idx = 0
#         while idx < len(num_str):
            
#             if optimal[idx][1] == idx:
#                 idx += 1
#                 continue
            
#             t = num_str[idx]
#             num_str[idx] = str(optimal[idx][0])
#             num_str[optimal[idx][1]] = t
#             return int("".join(num_str))
#             break
            
        
#         return num