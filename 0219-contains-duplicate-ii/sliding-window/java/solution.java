class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> window = new HashSet<>();
        int left = 0;

        for (int num : nums) { 
            if (window.contains(num)) { 
                return true;
            } 
            window.add(num); 

            if (window.size() > k) { 
                window.remove(nums[left]);
                left++;
            } 
        } 
        return false;
    }
}
