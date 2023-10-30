class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_n = len(flowerbed)
        count = 0
        
        for i in range(bed_n):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == bed_n - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    
                    if count >= n:
                        return True
                    
        return count >= n
        