class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        cows = 0
        bulls = 0
        count = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows += 1
            else:
                if count[int(secret[i])] < 0:
                    bulls += 1
                if count[int(guess[i])] > 0:
                    bulls += 1
                count[int(secret[i])] += 1
                count[int(guess[i])] -= 1
        
        return f"{cows}A{bulls}B"