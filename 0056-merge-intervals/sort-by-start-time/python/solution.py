class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if prev_end >= start: # overlapping
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res
