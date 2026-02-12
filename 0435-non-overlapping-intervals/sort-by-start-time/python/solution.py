class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                res += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
        return res
