class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false;
        }
        
        Map<Long, Long> buckets = new HashMap<>(); // Hashmap to store {bucketId -> num} in the sliding window
        long bucketSize = (long) valueDiff + 1; // Ensures numbers in the same bucket are within valueDiff
        int left = 0;
        for (int right = 0; right < nums.length; ++right) {
            long num = nums[right];
            long bucketId = Math.floorDiv(num, bucketSize);

            // Check if the current bucket already has a number
            if (buckets.containsKey(bucketId)) {
                return true;
            }
            
            // Note: Adjacent buckets might also contain numbers within valueDiff of the current num, as they may be close enough to satisfy the condition
            
            // Check left adjacent bucket
            if (buckets.containsKey(bucketId - 1) && Math.abs(num - buckets.get(bucketId - 1)) <= valueDiff) {
                return true;
            }

            // Check right adjacent bucket
            if (buckets.containsKey(bucketId + 1) && Math.abs(num - buckets.get(bucketId + 1)) <= valueDiff) {
                return true;
            }
            
            buckets.put(bucketId, num); // Add current num to its bucket in the sliding window

            // Ensure sliding window size does not exceed indexDiff, by removing the oldest number if needed
            if (right - left >= indexDiff) {
                long oldestNum = (long)nums[left];
                long oldestBucketId = Math.floorDiv(oldestNum, bucketSize);
                buckets.remove(oldestBucketId);
                left++;
            }
        }
        return false;
    }
}
