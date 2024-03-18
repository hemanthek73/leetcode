class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        result=1
        cur_start,cur_end=points[0][0],points[0][1]

        for start_pt,end_pt in points:
            if cur_end <start_pt:
                result+=1
                cur_start,cur_end=start_pt,end_pt
        return result
        