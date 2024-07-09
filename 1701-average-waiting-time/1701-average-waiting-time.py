class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg = 0
        
        curr = 0
        for a, t in customers:
            if curr <= a:
                curr = a + t
                avg += t
            else:
                avg += curr - a + t
                curr += t
        
        return avg / len(customers)
            
            
            