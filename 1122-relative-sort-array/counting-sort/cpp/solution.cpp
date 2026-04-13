class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        int max_num = *max_element(arr1.begin(), arr1.end());
        vector<int> count(max_num + 1, 0);
        vector<int> res;

        // Count frequency of elements in arr1
        for (int num : arr1)
            count[num]++;

        // Relative Sorting using arr2
        for (int num : arr2) {
            while (count[num] > 0) {
                res.push_back(num);
                count[num]--;
            }
        }

        // Processing remaining elements in ascending order
        for (int num = 0; num <= max_num; num++) {
            while (count[num] > 0) {
                res.push_back(num); 
                count[num]--;
            }
        }
        return res;
    }
};
