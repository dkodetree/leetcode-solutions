class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();  // num -> idx 

        for (int idx = 0; idx < nums.length; idx++) {
            int num = nums[idx];
            int complement = target - num;

            if (seen.containsKey(complement)) {
                return new int[] { idx, seen.get(complement) };
            }
            seen.put(num, idx);
        }
        return new int[] {};
    }
}
