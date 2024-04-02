class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst,mapts={},{}
        for c1,c2 in zip(s,t):
            if((c1 in mapst and mapst[c1]!=c2) or (c2 in mapts and mapts[c2]!=c1)):
                return False
            mapst[c1]=c2
            mapts[c2]=c1
        return True
        