class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int left_sum = 0;

        for (int idx = 0; idx < nums.size(); ++idx) {
            int num = nums[idx];
            int right_sum = total - left_sum - num;
            if (left_sum == right_sum) {
                return idx;
            }
            left_sum += num;
        }

        return -1;
    }
};
