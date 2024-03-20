class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subdict={0:1}
        n=len(nums)
        count=0
        s=0
        for num in nums:
            s+=num
            if s-k in subdict:
                count+=subdict[s-k]
            if s in subdict:
                subdict[s]+=1
            else:
                subdict[s]=1
        return count

        