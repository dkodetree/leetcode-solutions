class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = [] # Stores intervals that are already double-booked

    def book(self, event_start: int, event_end: int) -> bool:
        # If new interval overlaps with the existing overlapped regions, then don't book
        for start, end in self.overlaps:
            if max(event_start, start) < min(event_end, end):
                return False
        
        # If there are any overlaps with the existing calendar, then add the overlapped region to the overlaps list
        for start, end in self.calendar:
            intersect_start, intersect_end = max(event_start, start), min(event_end, end)
            if intersect_start < intersect_end:
                self.overlaps.append((intersect_start, intersect_end))
        
        self.calendar.append((event_start, event_end)) # Accept the booking
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(event_start,event_end)
