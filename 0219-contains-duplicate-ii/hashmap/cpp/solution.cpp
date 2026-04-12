class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> indexMap;
        for (int idx = 0; idx < nums.size(); idx++) {
            int num = nums[idx];
            if (indexMap.find(num) != indexMap.end() && idx - indexMap[num] <= k) {
                return true;
            }
            indexMap[num] = idx;
        }
        return false;
    }
};
