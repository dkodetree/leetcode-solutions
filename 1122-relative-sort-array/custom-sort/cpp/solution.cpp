struct CustomOrder {
    const unordered_map<int, int>& orderMap;
    const int INF = numeric_limits<int>::max();

    CustomOrder(const unordered_map<int, int>& m) : orderMap(m) {}

    bool operator()(int a, int b) const {
        auto itA = orderMap.find(a);
        auto itB = orderMap.find(b);

        // If in arr2, use its index, otherwise, treat as INF
        int rankA = (itA != orderMap.end()) ? itA->second : INF;
        int rankB = (itB != orderMap.end()) ? itB->second : INF;

        // Primary sort by arr2 index, secondary sort by value (asc).
        return (rankA != rankB) ? rankA < rankB : a < b; 
    }
};

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> order;
        for (int idx = 0; idx < arr2.size(); idx++) 
            order[arr2[idx]] = idx;

        sort(arr1.begin(), arr1.end(), CustomOrder(order));
        return arr1;     
    }
};
