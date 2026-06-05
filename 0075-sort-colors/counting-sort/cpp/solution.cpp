class Solution {
public:
    void sortColors(vector<int>& nums) {
        int freq[3] = {0, 0, 0};
        for (int num : nums) {
            freq[num]++;
        }

        int idx = 0;
        for (int color = 0; color < 3; color++) {
            while (freq[color]) {
                nums[idx] = color;
                freq[color]--;
                idx++;
            }
        }
    }
};
