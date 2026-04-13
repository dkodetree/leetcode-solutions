class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> order;
        for (int idx = 0; idx < arr2.size(); idx++) 
            order[arr2[idx]] = idx;

        const int INF = numeric_limits<int>::max();

        sort(arr1.begin(), arr1.end(), [&](int a, int b) {
            auto itA = order.find(a);
            auto itB = order.find(b);
            // If in arr2, use its index, otherwise, treat as INF
            int rankA = (itA != order.end()) ? itA->second : INF;
            int rankB = (itB != order.end()) ? itB->second : INF;

            // Primary sort by arr2 index, secondary sort by value (asc).
            return (rankA != rankB) ? rankA < rankB : a < b;    
        });
        return arr1;     
    }
};
