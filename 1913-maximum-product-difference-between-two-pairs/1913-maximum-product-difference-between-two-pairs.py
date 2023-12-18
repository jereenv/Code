class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        smallest = second_smallest = 10**4 + 1
        biggest = second_biggest = 0
        
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
            
            if num < smallest:
                second_smallest = smallest
                smallest = num
            else:
                second_smallest = min(second_smallest, num)
            
        print(second_smallest, smallest, second_biggest, biggest)
        
        return biggest*second_biggest - smallest*second_smallest
        