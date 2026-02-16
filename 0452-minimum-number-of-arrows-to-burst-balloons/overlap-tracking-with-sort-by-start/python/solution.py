class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()   # Sort by start point
        arrows = 1
        prev_overlap_end = points[0][1] # Tracks the rightmost boundary of the current overlapping balloon group
        for start, end in points[1:]:
            if start <= prev_overlap_end:   # Overlap detected, so update overlap window
                prev_overlap_end = min(prev_overlap_end, end)
            else:       # No overlap, so we need another arrow for the new group
                arrows += 1
                prev_overlap_end = end
        return arrows
