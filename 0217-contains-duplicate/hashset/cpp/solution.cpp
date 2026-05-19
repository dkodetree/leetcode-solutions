class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> values_seen;
        for (int num : nums) {
            if (values_seen.count(num)) {
                return true;
            }
            values_seen.insert(num);
        }
        return false;
    }
};
