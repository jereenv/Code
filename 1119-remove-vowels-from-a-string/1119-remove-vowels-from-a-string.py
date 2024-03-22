class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        
        return "".join([x if x not in vowels else "" for x in s])
        