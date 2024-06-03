class Solution:
    
#     def first_occurrence(self, arr, x):

#         low = 0
#         high = len(arr) - 1
#         result = -1
#         while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#           low = mid + 1
#         elif arr[mid] == x:
#           result = mid
#           high = mid - 1  
#         else:
#           high = mid - 1
#         return result if result != -1 else len(arr)
    
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diff_arr = []
        
        for i, j in zip(nums1, nums2):
            diff_arr.append(i - j)
        
        diff_arr.sort()
        
        ans = 0
        
        n = len(diff_arr)
        l, r = 0, n - 1
        
        
        
#         while l < r:
#             s = diff_arr[l] + diff_arr[r]
#             if s > 0:

#                 r1 = r
#                 l1 = l
                
#                 while l1 < r1:
#                     s = diff_arr[l1] + diff_arr[r1]
#                     if s <= 0:
#                         break
#                     else:
#                         print(l1, r1)
                        
#                         r1 -= 1
#                 ans += n - r1
#                 l += 1
#                 r -= 1
#             elif s <= 0:
#                 l += 1
            
#         return ans


        N = len(nums1)  # nums2 is the same length

        # Difference[i] stores nums1[i] - nums2[i]
        difference = [nums1[i] - nums2[i] for i in range(N)]
        difference.sort()

        # Count the number of valid pairs
        result = 0
        for i in range(0, N):
            # All indices j following i make a valid pair
            if difference[i] > 0:
                result += N - i - 1
                
            # Binary search to find the first index j
            # that makes a valid pair with i
            else:
                left = i + 1
                right = N - 1
                while left <= right:
                    mid = (left + right) // 2
                    # If difference[mid] is a valid pair, search in left half
                    if difference[i] + difference[mid] > 0:
                        right = mid - 1
                    # If difference[mid] does not make a valid pair, search in right half
                    else:
                        left = mid + 1

                # After the search left points to the first index j that makes
                # a valid pair with i so we count that and all following indices
                result += N - left

        return result