class Solution {
public:
    bool isValid(string s) {
        int length;
        std::string cur_str = s;
        
        do
        {
            length = cur_str.length();
            size_t pos;
            if ((pos = cur_str.find("()")) != std::string::npos) {
                cur_str.erase(pos, 2);
            } else if ((pos = cur_str.find("[]")) != std::string::npos) {
                cur_str.erase(pos, 2);
            } else if ((pos = cur_str.find("{}")) != std::string::npos) {
                cur_str.erase(pos, 2);
            }
        } while (cur_str.length() < length);

        return cur_str.empty();
    }
};
