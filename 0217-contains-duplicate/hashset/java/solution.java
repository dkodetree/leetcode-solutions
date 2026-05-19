class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> valuesSeen = new HashSet<>();
        for (int num : nums) {
            // add() returns false if element already exists
            if (!valuesSeen.add(num)) {
                return true;
            }
        }
        return false;
    }
}
