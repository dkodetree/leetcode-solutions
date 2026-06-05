class Solution {
    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int idx = 0;

        while (idx <= right) { // Important condition
            if (nums[idx] == 0) {
                swap(nums, left, idx); // Swap with left
                left++;
                idx++;
            } else if (nums[idx] == 1) { // No swap needed for 1
                idx++;
            } else {    // nums[idx] == 2
                swap(nums, idx, right); // Swap with right
                right--;
            }
        }
    }

    // Helper to swap elements
    private void swap(int[] nums, int idx1, int idx2) {
        int temp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = temp;
    }
}
