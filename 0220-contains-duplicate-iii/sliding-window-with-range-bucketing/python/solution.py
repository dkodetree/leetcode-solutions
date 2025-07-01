class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        buckets = collections.defaultdict(int)      # Hashmap to store {bucket_id -> num} in the sliding window
        bucket_size = valueDiff + 1                 # Ensures numbers in the same bucket are within valueDiff

        left = 0
        for right, num in enumerate(nums):
            bucket_id = num // bucket_size      # Python automatically floors integer division for negative numbers
            
            if bucket_id in buckets:            # Check if the current bucket already has a number
                return True
            
            # Check adjacent buckets for numbers within valueDiff of the current num, as they may be close enough to satisfy the condition
            for adj_id in (bucket_id - 1, bucket_id + 1):   
                if adj_id in buckets and abs(num - buckets[adj_id]) <= valueDiff:
                    return True

            buckets[bucket_id] = num    # Add current num to its bucket in the sliding window

            # Ensure window size does not exceed indexDiff, by removing the oldest number if needed (sliding window)
            if right - left >= indexDiff:
                old_num = nums[left]
                old_bucket_id = old_num // bucket_size
                del buckets[old_bucket_id]
                left += 1

        return False
