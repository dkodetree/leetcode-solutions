class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<string> res;
        unordered_set<char> left;
        unordered_map<char, int> right;
        for (char ele : s) {
            right[ele]++;
        }

        for (char mid : s) {    // atmost n
            right[mid]--;
            for (char outer : left) {   // atmost 26
                if (right[outer] > 0) {
                    res.insert(string(1, outer) + mid);
                }
            }
            left.insert(mid);
        }
        return res.size();
    }
};
