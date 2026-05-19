class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int idx = 1; idx < nums.length; idx++) {
            if (nums[idx] == nums[idx - 1]) {
                return true;
            }
        }
        return false;
    }
}
