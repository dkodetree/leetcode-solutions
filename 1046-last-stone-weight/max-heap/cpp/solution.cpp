class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // priority_queue in C++ is max-heap by default
        priority_queue<int> max_heap(stones.begin(), stones.end());
        
        while (max_heap.size() > 1) {
            int first_stone = max_heap.top();
            max_heap.pop();
            
            int second_stone = max_heap.top();
            max_heap.pop();
            
            if (first_stone != second_stone) {
                max_heap.push(first_stone - second_stone);
            }
        }
        return max_heap.empty() ? 0 : max_heap.top();
    }
};
