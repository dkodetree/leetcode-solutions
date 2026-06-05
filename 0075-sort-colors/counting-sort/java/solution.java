class Solution {
    public void sortColors(int[] nums) {
        int[] freq = new int[3];
        for (int num : nums) {
            freq[num]++;
        }

        int idx = 0;
        for (int color = 0; color < 3; color++) {
            while (freq[color] > 0) {
                nums[idx] = color;
                freq[color]--;
                idx++;
            }
        }
    }
}
