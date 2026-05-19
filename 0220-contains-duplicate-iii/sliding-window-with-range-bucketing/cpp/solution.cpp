class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }

        unordered_map<long long, long long> buckets;    // Hashmap to store {bucket_id -> num} in the sliding window
        long long bucket_size = (long long)valueDiff + 1;   // Ensures numbers in the same bucket are within valueDiff
        int left = 0;
        for (int right = 0; right < nums.size(); right++) {
            long long num = nums[right];
            long long bucket_id = num >= 0 ? num / bucket_size : ((num + 1) / bucket_size) - 1;   // Floor division   

            // Check if the current bucket already has a number
            if (buckets.find(bucket_id) != buckets.end()) {
                return true;
            }

            // Note: Adjacent buckets might contain numbers within valueDiff of the current num, as they may be close enough to satisfy the condition
            
            // Check left adjacent bucket
            if (buckets.find(bucket_id - 1) != buckets.end() && abs(num - buckets[bucket_id - 1]) <= valueDiff) {
                return true;
            }

            // Check right adjacent bucket
            if (buckets.find(bucket_id + 1) != buckets.end() && abs(num - buckets[bucket_id + 1]) <= valueDiff) {
                return true;
            }

            buckets[bucket_id] = num;   // Add current num to its bucket in the sliding window

            // Ensure sliding window size does not exceed indexDiff, by removing the oldest number if needed
            if (right - left >= indexDiff) {
                long long oldest_num = nums[left];
                long long oldest_bucket_id = oldest_num >= 0 ? oldest_num / bucket_size : ((oldest_num + 1) / bucket_size) - 1;     // Floor division  
                buckets.erase(oldest_bucket_id);
                left++;
            }
        }
        return false;
    }
};
