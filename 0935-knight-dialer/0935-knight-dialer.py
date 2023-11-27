class Solution:
    
    ans = 0
    def knightDialer(self, n: int) -> int:
        
        paths = {
            0: [4,6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2]
        }
        
        memo = {}
        
        def depth(d, curr):
            
            if (d, curr) in memo:
                return memo[(d, curr)]
            
            if d == n:
                return 1
            
            temp = 0
            
            
            for i in paths[curr]:
                temp += depth(d + 1, i)
            
            memo[(d, curr)] = temp
            
            return memo[(d, curr)] 
        
        temp = 0
        for i in range(10):
            temp += depth(1, i)
        return temp % (10**9 + 7)
            
        
#         dialer = [[True]*3]*4
#         print(dialer)
#         dialer[3][0] = False
#         dialer[3][2] = False
        
# #         print("dialer: ", dialer)

#         dialer = []
#         for row in range(4):
#             temp = []
#             for col in range(3):
#                 temp.append(True)
#             dialer.append(temp)
        
#         dialer[3][0] = False
#         dialer[3][2] = False
    
        
#         def dp(curr, i, j):

#             if i < 0 or i > 3:
#                 return
            
#             if j < 0 or j > 2:
#                 return
            
#             if not dialer[i][j]:
#                 return
            
#             if curr == n:
                
#                 self.ans += 1
#                 return
            
#             dp(curr + 1, i + 2, j - 1)
#             dp(curr + 1, i - 2, j - 1)
#             dp(curr + 1, i - 1, j + 2)
#             dp(curr + 1, i - 1, j - 2)
        
#         print(dialer)
#         for row in range(4):
#             for col in range(3):
#                 print(dialer[row][col], row, col)
#                 if dialer[row][col]:
#                     print(row, col)
#                     dp(1, row, col)
#         return self.ans


    