class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = new_interval

        for start, end in intervals:
            if end < new_start:     # Current interval ends before new interval starts
                res.append([start, end])
            elif new_end < start:   # New interval ends before current interval starts
                res.append([new_start, new_end])
                new_start, new_end = start, end
            else:                   # Intervals Overlap, so merge with the rolling new interval
                new_start, new_end = min(start, new_start), max(end, new_end)

        res.append([new_start, new_end])    # Append the final left over rolling interval
        return res
