class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }

        TreeSet<Long> window = new TreeSet<>(); // Maintain a sorted sliding window
        int left = 0;
        for (long num : nums) {
            // Find the smallest number in the window that is ≥ (num - valueDiff), as a potential nearby almost duplicate
            Long ceiling = window.ceiling(num - valueDiff);

            // Check if that number is within valueDiff of current num
            if (ceiling != null && Math.abs(num - ceiling) <= valueDiff) {
                return true;
            }

            window.add(num);            
            // Ensure window size does not exceed indexDiff. Note: Duplicates are handled by the early return above.
            if (window.size() > indexDiff) { 
                window.remove((long) nums[left]);
                left++;
            }   
        }       
        return false;
    }
}
