class Solution:
    def longestPalindrome(self, s):
        dic = {}
        for i in s:
            dic[i] = 1 + dic.get(i,0)
        
        count = 0
        m = 0
        for i in dic:
            count += dic[i]
            if dic[i] % 2 != 0:
                count -= 1
                if m == 0:
                    m = 1
                    count += 1
        return count