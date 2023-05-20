class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     if not s[r].isalnum():
        #         r -= 1
        #     if not s[l].isalnum():
        #         l += 1
        #     if s[r].isalnum() and s[l].isalnum():
        #         if s[r].lower() != s[l].lower():
        #             return False
        #         l += 1
        #         r -= 1
        # return True
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        return newStr == newStr[::-1]