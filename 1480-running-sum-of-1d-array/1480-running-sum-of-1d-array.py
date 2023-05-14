class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        retSum=[]
        for i in nums:
            sums+=i
            retSum.append(sums)
        return retSum
        