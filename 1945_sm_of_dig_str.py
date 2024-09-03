class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for x in s:
            num+=str(ord(x)-ord('a')+1)
        for _ in range(k):
            s=0
            for x in num:
                s+=int(x)
            num=str(s)
        return int(num)