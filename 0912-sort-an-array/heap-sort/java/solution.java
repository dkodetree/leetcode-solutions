class Solution {
    private void maxHeapify(int[] nums, int idx, int heapSize) {     // O(log n)
        int largest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;

        if (left < heapSize && nums[left] > nums[largest]) {
            largest = left;
        }
        if (right < heapSize && nums[right] > nums[largest]) {
            largest = right;
        }

        if (largest != idx) {
            int temp = nums[idx];
            nums[idx] = nums[largest];
            nums[largest] = temp;

            maxHeapify(nums, largest, heapSize);
        }
    }

    private void buildHeap(int[] nums, int heapSize) {  // O(n)
        for (int idx = heapSize / 2 - 1; idx >= 0; idx--) {
            maxHeapify(nums, idx, heapSize);
        }
    }

    private void heapSort(int[] nums) { // O(n log n)
        int heapSize = nums.length;
        buildHeap(nums, heapSize);

        for (int idx = nums.length - 1; idx > 0; idx--) {   // from n-1 down to 1 (leaving index 0, which ends up in correct place)
            int temp = nums[0];
            nums[0] = nums[idx];
            nums[idx] = temp;

            heapSize--;
            maxHeapify(nums, 0, heapSize);
        }
    }

    public int[] sortArray(int[] nums) {
        heapSort(nums);
        return nums;
    }
}
