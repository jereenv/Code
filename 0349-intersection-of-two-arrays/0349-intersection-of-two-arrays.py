class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        
        l, r = 0, 0
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                ans.append(nums1[l])
                while l < len(nums1)  and nums1[l] == ans[-1]:
                    l += 1
                while r < len(nums2) and nums2[r] == ans[-1]:
                    r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return ans
        