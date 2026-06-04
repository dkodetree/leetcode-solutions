class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> ans_freq_map;
        for (int ans : answers) {
            ans_freq_map[ans]++;
        }
        int total_rabbits = 0;
        for (auto const& [ans, freq] : ans_freq_map) {
            int group_size = ans + 1;
            int num_groups = ceil(double(freq) / group_size); 
            total_rabbits += num_groups * group_size;
        }
        return total_rabbits;
    }
};
