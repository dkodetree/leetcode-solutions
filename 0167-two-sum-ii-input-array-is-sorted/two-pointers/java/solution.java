class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int curSum = numbers[left] + numbers[right];

            if (curSum > target) {
                right--;
            }
            else if (curSum < target) {
                left++;
            }
            else {
                return new int[] {left + 1, right + 1};
            } 
        }
        return new int[] {};
    }
}
