class RecentCounter {
    private final Deque<Integer> requests;

    public RecentCounter() {
        this.requests = new ArrayDeque<>();
    }
    
    public int ping(int t) {
        // Add new request timestamp
        requests.addLast(t);
        
        // Remove timestamps older than t - 3000
        while (!requests.isEmpty() && requests.peekFirst() < t - 3000) {
            requests.removeFirst();
        }
        
        // Queue size represents the number of pings in the range [t-3000, t]
        return requests.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
