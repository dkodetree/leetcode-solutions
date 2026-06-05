class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int idx = 0;

        while (idx <= right) {  // Important condition
            if (nums[idx] == 0) {
                swap(nums[left], nums[idx]); // Swap with left
                left++;
                idx++;
            }
            else if (nums[idx] == 1) {  // No swap needed for 1
                idx++;
            }
            else {  // nums[idx] == 2
                swap(nums[idx], nums[right]); // Swap with right
                right--;
            }
        }
    }
};
