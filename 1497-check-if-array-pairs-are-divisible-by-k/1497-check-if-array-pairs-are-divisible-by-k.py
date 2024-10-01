class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        s = sum(arr)
        
        size = n // 2
        
        dic = defaultdict(int)
        
        for i in arr:
            dic[i % k] += 1
        
        
        for num in dic:
            if num == 0:
                pass
            
            elif num == k/2:
                if dic[num] % 2 != 0:
                    return False
            
            else:
                if dic[num] != dic[k - num]:
                    return False
            
        return True
                
        