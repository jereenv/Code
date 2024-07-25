class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            idx1 = 0
            idx2 = 0
            
            arr = []
            
            n1 = len(left)
            n2 = len(right)
            
            while idx1 < n1 and idx2 < n2:
                if left[idx1] < right[idx2]:
                    arr.append(left[idx1])
                    idx1 += 1
                else:
                    arr.append(right[idx2])
                    idx2 += 1
            
            if idx1 == n1:
                arr.extend(right[idx2:])
            
            if idx2 == n2:
                arr.extend(left[idx1:])
            
            return arr
        
        def divide(arr):
            
            if len(arr) > 1:
                n = len(arr)
                left = divide(arr[:n//2])
                right = divide(arr[n//2:])
                
                arr = merge(left, right)
            
            return arr
        
        return divide(nums)
                
            
            