class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        p, q  = 0, 0
        while p < len(firstList) and q < len(secondList):
            start1, end1 = firstList[p]
            start2, end2 = secondList[q]

            intersect_start, intersect_end = max(start1, start2), min(end1, end2)
            if intersect_start <= intersect_end: # overlap
                res.append([intersect_start, intersect_end])
            
            if end1 < end2:
                p += 1
            else:
                q += 1
        return res
