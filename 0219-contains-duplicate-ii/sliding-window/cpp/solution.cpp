class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;
        int left = 0; 
        
        for (int num : nums) { 
            if (window.count(num)) { 
                return true; 
            }
            window.insert(num);

            if (window.size() > k) {
                window.erase(nums[left]);
                left++; 
            }
        }
        return false;
    }
};
