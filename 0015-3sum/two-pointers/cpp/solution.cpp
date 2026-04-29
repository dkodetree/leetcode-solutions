class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            // Its impossible to get a triplet summing to 0 after the first number becomes +ve    
            if (nums[i] > 0) {
                break;
            }

            // Skip duplicates for the first number
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int cur_sum = nums[i] + nums[left] + nums[right];

                if (cur_sum < 0) {
                    left++;
                } else if (cur_sum > 0) {
                    right--;
                } else {
                    res.push_back({nums[i], nums[left], nums[right]});  // Found a valid triplet

                    // Move both pointers and skip duplicates
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1])  {
                        right--;
                    }
                }
            }
        }
        return res;
    }
};
