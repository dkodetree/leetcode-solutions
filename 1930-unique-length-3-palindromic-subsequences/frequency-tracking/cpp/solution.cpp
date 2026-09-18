class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<int> res;
        unordered_set<char> left;
        vector<int> right(26, 0);
        for (char ele : s) {
            right[ele - 'a']++;
        }

        for (char mid : s) {    // at most n
            int mid_idx = mid - 'a';
            right[mid_idx]--; 

            for (char outer : left) {   // at most 26
                int outer_idx = outer - 'a';
                if (right[outer_idx] > 0) {
                    res.insert(outer_idx * 26 + mid_idx); // encoding (outer, mid) as an unique integer
                }
            }
            left.insert(mid); 
        }
        return res.size();
    }
};
