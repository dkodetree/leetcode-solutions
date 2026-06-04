class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        return countPairs(nums, upper) - countPairs(nums, lower - 1);
    }

private:
    // Helper to count pairs with sum less than or equal to upper_bound
    long long countPairs(const vector<int>& nums, int upper_bound) {
        long long count = 0;
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int pair_sum = nums[left] + nums[right];
            if (pair_sum <= upper_bound) {
                count += (right - left);
                left++;
            } else {
                right--;
            }
        }
        return count;
    }
    
};
