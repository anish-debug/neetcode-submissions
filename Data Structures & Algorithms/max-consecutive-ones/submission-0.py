class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) >=1 and len(nums)<=pow(10,5):
            c,maxm=0,0
            for elm in nums:
                if elm == 1:
                    c=c+1
                else:
                    c=0
                if c>maxm:
                    maxm=c
            return maxm
        