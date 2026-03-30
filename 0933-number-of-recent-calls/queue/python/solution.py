class RecentCounter:

    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        # Add new request timestamp
        self.requests.append(t)

        # Remove timestamps older than t - 3000
        while (self.requests[0] < t - 3000):
            self.requests.popleft()
        
        # Queue size represents the number of pings in the range [t-3000, t]
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
