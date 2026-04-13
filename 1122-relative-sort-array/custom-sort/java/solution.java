class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // Map for rank lookups
        Map<Integer, Integer> order = new HashMap<>();  
        for (int idx = 0; idx < arr2.length; idx++) 
            order.put(arr2[idx], idx);
        
        // Explicit Boxing (Required for custom Comparator support)
        Integer[] boxed = new Integer[arr1.length]; 
        for (int idx = 0; idx < arr1.length; idx++) 
            boxed[idx] = arr1[idx];

        // Custom Comparator
        Comparator<Integer> customComparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int rankA = order.getOrDefault(a, Integer.MAX_VALUE);
                int rankB = order.getOrDefault(b, Integer.MAX_VALUE);
    
                return (rankA != rankB) ? rankA - rankB : a - b;
            }
        };

        // Sorting 
        Arrays.sort(boxed, customComparator);

        // Explicit Unboxing
        for (int idx = 0; idx < arr1.length; idx++)
            arr1[idx] = boxed[idx];
        
        return arr1;
    }
}
