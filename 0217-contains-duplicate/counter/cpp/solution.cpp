class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            if (++freq[num] > 1) {
                return true;
            }
        }
        return false;
    }
};
