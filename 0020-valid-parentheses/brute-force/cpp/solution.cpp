class Solution {
public:
    bool isValid(string s) {
        int prev_length;
        std::string cur_str = s;
        
        do
        {
            prev_length = cur_str.length();
            size_t pos;
            if ((pos = cur_str.find("()")) != std::string::npos) {
                cur_str.erase(pos, 2);
            } else if ((pos = cur_str.find("[]")) != std::string::npos) {
                cur_str.erase(pos, 2);
            } else if ((pos = cur_str.find("{}")) != std::string::npos) {
                cur_str.erase(pos, 2);
            }
        } while (cur_str.length() < prev_length);

        return cur_str.empty();
    }
};
