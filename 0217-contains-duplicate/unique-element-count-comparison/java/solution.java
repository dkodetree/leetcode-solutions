class Solution {
    public boolean containsDuplicate(int[] nums) {
        return nums.length > Arrays.stream(nums).distinct().count();
    }
}
