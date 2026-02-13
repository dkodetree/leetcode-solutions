from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start_time: int, end_time: int) -> bool:
        idx = self.calendar.bisect_left((start_time, end_time))
        
        if idx - 1 >= 0:
            prev_end = self.calendar[idx - 1][1]
            if start_time < prev_end:    # overlaps with previous interval
                return False
        
        if idx < len(self.calendar):
            next_start = self.calendar[idx][0]
            if next_start < end_time:    # overlaps with next interval
                return False

        self.calendar.add((start_time, end_time))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
