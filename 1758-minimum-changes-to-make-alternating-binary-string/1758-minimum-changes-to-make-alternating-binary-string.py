class Solution:
    def minOperations(self, s: str) -> int:
        flag = True
        ans1 = 0
        ans2 = 0
        for i in s:
            if flag:
                if i != "1":
                    ans1 += 1
            if not flag:
                if i != "0":
                    ans1 += 1
            flag = not flag
        flag = True
        for i in s:
            if flag:
                if i != "0":
                    ans2 += 1
            if not flag:
                if i != "1":
                    ans2 += 1
            flag = not flag
        print(ans1, ans2)
        return min(ans1, ans2)