class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                result += tickets[i]
            elif i <= k and tickets[i] >= tickets[k]:
                result += tickets[k]
            else:
                result += tickets[k] - 1
        return result