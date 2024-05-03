class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1_list=v1.split('.')
        v2_list=v2.split('.')
        len1=len(v1_list)
        len2=len(v2_list)
        for i in range(max(len1,len2)):
            i1=int(v1_list[i]) if i<len1 else 0
            i2=int(v2_list[i]) if i<len2 else 0
            if i1!=i2:
                return 1 if i1>i2 else -1
        return 0