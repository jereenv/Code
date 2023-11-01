class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        ans, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            
            ans.append(s[j+1: j + 1 + word_len])
            
            i = j + 1 + word_len
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))