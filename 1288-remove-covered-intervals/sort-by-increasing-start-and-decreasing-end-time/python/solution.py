class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start time ascending. Break ties by end time descending to detect coverage correctly.
        intervals.sort(key=lambda x: (x[0], - x[1])) 

        covered = 0
        prev_start, prev_end = intervals[0]
        for start, end in intervals[1:]:
            if prev_start <= start and end <= prev_end:
                covered += 1
            else:
                prev_end = end

        return len(intervals) - covered
