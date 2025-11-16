class RecentCounter:

    def __init__(self):
        self.recent_counter = collections.deque()

    def ping(self, t: int) -> int:
        self.recent_counter.append(t)

        while (self.recent_counter[0] < t - 3000):
            self.recent_counter.popleft()
        
        return len(self.recent_counter)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
