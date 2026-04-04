class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) 
            return false;

        unordered_map<char, char> s_to_t_map;
        unordered_map<char, char> t_to_s_map;

        for (int idx = 0; idx < s.length(); idx++) {
            char char1 = s[idx];
            char char2 = t[idx];

            if (s_to_t_map.count(char1) && s_to_t_map[char1] != char2) 
                return false;
            
            if (t_to_s_map.count(char2) && t_to_s_map[char2] != char1)
                return false;

            s_to_t_map[char1] = char2;
            t_to_s_map[char2] = char1;
        }
        return true;
    }
};
