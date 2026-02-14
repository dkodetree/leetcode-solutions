from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.bookings = SortedDict()    # Store the booking count changes at each point in time on a sorted timeline

    def book(self, start: int, end: int) -> int:
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1

        k = 0   # Max Concurrent
        running_count = 0
        for change in self.bookings.values():
            running_count += change
            k = max(k, running_count)
        return k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
