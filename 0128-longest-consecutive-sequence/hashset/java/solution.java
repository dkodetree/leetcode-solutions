class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);
        }

        int maxLength = 0;
        for (int num : numsSet) {
            if (!numsSet.contains(num - 1)) { // num is start of a sequence
                int length = 1;
                while (numsSet.contains(num + length)) {
                    length++;
                }
                maxLength = Math.max(maxLength, length);
            }
        }
        return maxLength;
    }
}
