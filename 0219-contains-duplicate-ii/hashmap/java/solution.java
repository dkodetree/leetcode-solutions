class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> indexMap = new HashMap<>();
        for (int idx = 0; idx < nums.length; idx++) {
            int num = nums[idx];
            if (indexMap.containsKey(num) && idx - indexMap.get(num) <= k) {
                return true;
            }
            indexMap.put(num, idx);
        }
        return false;
    }
}
