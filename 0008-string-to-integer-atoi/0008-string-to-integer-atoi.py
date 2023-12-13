class Solution:
    def myAtoi(self, s: str) -> int:
        
        digits = set()
        for i in range(10):
            digits.add(str(i))
        
        symbols = set()
        symbols.add("-")
        symbols.add("+")
        
        ans = []
        ctr = 0
        for i in s:

            if i in digits:
                if not ans:
                    ans.append([])
                ans[ctr].append(i)
            elif i in symbols:
                if not ans:
                    ans.append([])
                ans.append([])
                ctr += 1
                ans[ctr].append(i)
            elif i == " " and not ans:
                pass
            else:
                break
        
        for idx, val in enumerate(ans):
            if not val:
                ans.pop(idx)
        
        temp = 1
        t2 = 0
        print(ans)
        for i in ans:
            if i:
                if i[0] == "-":
                    temp = -1
                    i.pop(0)
                    # t2 += 1
                elif i[0] == "+":
                    i.pop(0)
                if not i or i[0] not in digits:
                    return 0
                
                res = int("".join(i[t2:]))*temp
                if (2 ** 31) * (-1) < res < (2 ** 31):
                    return res
                if res <= (2 ** 31) * (-1):
                    return (2 ** 31) * (-1) 
                else:
                    return (2 ** 31) - 1
        return 0
        