class RecentCounter {
private:
    std::queue<int> requests;
public:
    RecentCounter() {
        // Constructor is empty as the queue initializes itself
    }
    
    int ping(int t) {
        // Add new request timestamp
        requests.push(t);
        
        // Remove timestamps older than t - 3000
        while (!requests.empty() && requests.front() < t - 3000) {
            requests.pop();
        }
        
        // Queue size represents the number of pings in the range [t-3000, t]
        return requests.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
