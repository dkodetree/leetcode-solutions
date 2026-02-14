from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.bookings = SortedDict()    # Store the changes at each point in time on a sorted timeline

    def book(self, start: int, end: int) -> bool:
        # Tentatively add the new event
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1

        running_count = 0
        for change in self.bookings.values():
            running_count += change
            if running_count > 2:   # Triple booking detected
                # Rollback tentative changes
                self.bookings[start] = self.bookings.get(start, 0) - 1
                self.bookings[end] = self.bookings.get(end, 0) + 1

                # Clean up zero-delta entries for both boundaries
                if self.bookings[start] == 0:
                    self.bookings.pop(start)
                if self.bookings[end] == 0:
                    self.bookings.pop(end)
                
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
