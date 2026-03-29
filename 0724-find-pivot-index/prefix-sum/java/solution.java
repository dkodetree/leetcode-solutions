class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int leftSum = 0;
        for (int idx = 0; idx < nums.length; idx++) {
            int rightSum = totalSum - leftSum - nums[idx];
            if (leftSum == rightSum) {
                return idx;
            }
            leftSum += nums[idx];
        }

        return -1;
    }
}
