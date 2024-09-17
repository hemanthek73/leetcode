class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        str1=s1.split(' ')
        str2=s2.split(' ')
        total=str1+str2
        ans=[x for x in set(total) if total.count(x)==1]
        return ans
