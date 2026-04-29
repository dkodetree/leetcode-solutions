class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int numsLength = nums.length;

        for (int i = 0; i < numsLength; i++) {
            // Its impossible to get a triplet summing to 0 after the first number becomes +ve
            if (nums[i] > 0) {
                break;
            }

            // Skip duplicates for the first number
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = numsLength - 1;
            while (left < right) {
                int curSum = nums[i] + nums[left] + nums[right];

                if (curSum < 0) {
                    left++;
                } else if (curSum > 0) {
                    right--;
                } else {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));   // Found a valid triplet

                    // Move both pointers and skip duplicates
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
            }
        }
        return res;
    }
}
