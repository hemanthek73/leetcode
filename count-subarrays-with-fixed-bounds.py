class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minFound=False
        maxFound=False

        start=0
        minstart=0
        maxstart=0
        count=0

        for i,num in enumerate(nums):
            if num>maxK or num<minK:
                minFound=False
                maxFound=False
                start=i+1

            if num==minK:
                minstart=i
                minFound=True

            if num==maxK:
                maxstart=i
                maxFound=True

            if minFound and maxFound:
                count+=min(minstart,maxstart)-start+1
        return count