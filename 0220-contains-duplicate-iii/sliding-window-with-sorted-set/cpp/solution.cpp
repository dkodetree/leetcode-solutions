class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }

        set<long long> window;  // maintains a sorted sliding window
        int left = 0;
        for (long long num : nums) {
            // Find the smallest number in the window that is ≥ (num - valueDiff), as a potential nearby almost duplicate
            auto it = window.lower_bound(num - valueDiff);
            
            // Check if that number is within valueDiff of current num
            if (it != window.end() && abs(num - *it) <= valueDiff) {
                return true;
            }
                    
            window.insert(num);
            // Ensure window size does not exceed indexDiff
            if (window.size() > indexDiff) { 
                window.erase(nums[left]);
                left++;
            }          
        }
        return false;
    }
};
