class Solution:
    def partitionString(self, s: str) -> int:
        s1 = set()
        count = 1
        for i in s:
            if i in s1:
                count += 1
                s1 = set()
            s1.add(i)
        return count
        