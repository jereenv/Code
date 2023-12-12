class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        flag = 0
        ctr = 0
        for i in s:
            print(flag, ctr)
            if flag == 0:
                arr[ctr].append(i)
                ctr += 1
                if ctr == numRows:
                    flag = 1
                    ctr -= 2
            else:
                arr[ctr].append(i)
                ctr -= 1
                if ctr <= -1:
                    ctr += 2
                    flag = 0
        print(arr)
        ans = ["".join(i) for i in arr]
        return "".join(ans)
                    
            
            
            