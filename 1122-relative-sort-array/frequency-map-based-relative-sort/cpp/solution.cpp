class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int, int> freq_map;
        for (int num : arr1) 
            freq_map[num]++;

        vector<int> res;

        // Add elements in the order defined by arr2, and remove from the frequency map
        for (int num : arr2) {
            if (freq_map.count(num)) {
                int count = freq_map[num];
                res.insert(res.end(), count, num);
                freq_map.erase(num);  
            }
        }

        // Add remaining elements in ascending order
        for (auto const& [val, count] : freq_map) {
            res.insert(res.end(), count, val);
        }
        return res;
    }
};
