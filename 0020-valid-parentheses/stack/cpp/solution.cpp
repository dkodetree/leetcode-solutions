class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> bracket_map = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        std::stack<char> open_bracket_stack;
        for (char ele : s) {
            if (bracket_map.count(ele)) {     // close
                if (open_bracket_stack.empty() || open_bracket_stack.top() != bracket_map[ele]) {
                    return false;
                }
                open_bracket_stack.pop();
            } 
            else {      // open
                open_bracket_stack.push(ele);
            }
        }
        return open_bracket_stack.empty();
    }
};
