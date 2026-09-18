class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int max_length = 0;
        for (int num : nums_set) {
            if (nums_set.find(num - 1) == nums_set.end()) { // num is start of sequence
                int length = 1;
                while (nums_set.find(num + length) != nums_set.end()) {
                    length++;
                }
                max_length = max(max_length, length);
            }
        }
        return max_length;
    }
};
