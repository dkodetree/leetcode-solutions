class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Find intersection point
        int slow = 0;
        int fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        // Phase 2: Find entrance to the cycle (the duplicate number)
        int slow1 = 0;
        while (slow != slow1) {
            slow = nums[slow];
            slow1 = nums[slow1];
        }
        return slow;
    }
}
