class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int maxNum = 0;
        for (int num : arr1) 
            maxNum = Math.max(maxNum, num);
        
        // Count frequency of elements in arr1
        int[] count = new int[maxNum + 1];
        for (int num : arr1) 
            count[num]++;
        
        int[] res = new int[arr1.length];
        int index = 0;
        
        // Relative Sorting using arr2
        for (int num : arr2) {
            while (count[num] > 0) {
                res[index++] = num;
                count[num]--;
            }
        }

        // Processing remaining elements in ascending order
        for (int num = 0; num <= maxNum; num++) {
            while (count[num] > 0) {
                res[index++] = num;
                count[num]--;
            }
        }
        return res;
    }
}
