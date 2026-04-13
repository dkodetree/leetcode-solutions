class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        TreeMap<Integer, Integer> freqMap = new TreeMap<>();
        for (int num : arr1) 
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);

        int[] res = new int[arr1.length];
        int idx = 0;

        // Add elements in the order defined by arr2, and remove from the frequency map
        for (int num : arr2) {
            Integer count = freqMap.remove(num);
            if (count != null) {
                while (count-- > 0) 
                    res[idx++] = num;
            }
        }

        // Add remaining elements in ascending order
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int count = entry.getValue();
            int val = entry.getKey();
            for (int i = 0; i < count; i++) {
                res[idx++] = val;
            }
        }
        return res;
    }
}
