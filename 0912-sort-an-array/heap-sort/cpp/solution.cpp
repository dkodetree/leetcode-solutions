class Solution {
private:
    void maxHeapify(vector<int>& nums, int idx, int heap_size) {   // O(log n)
        int largest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;

        if (left < heap_size && nums[left] > nums[largest]) {
            largest = left;
        }
        if (right < heap_size && nums[right] > nums[largest]) {
            largest = right;
        }

        if (largest != idx) {
            swap(nums[idx], nums[largest]);
            maxHeapify(nums, largest, heap_size);
        }
    }

    void buildHeap(vector<int>& nums, int heap_size) {    // O(n)
        for (int idx = heap_size / 2 - 1; idx >= 0; idx--) {
            maxHeapify(nums, idx, heap_size);
        }
    }

    void heapSort(vector<int>& nums) { // O(n log n)
        int heap_size = nums.size();
        buildHeap(nums, heap_size);
        
        for (int idx = nums.size() - 1; idx > 0; idx--) {
            swap(nums[0], nums[idx]);
            heap_size--;
            maxHeapify(nums, 0, heap_size);
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        heapSort(nums);
        return nums;
    }
};
