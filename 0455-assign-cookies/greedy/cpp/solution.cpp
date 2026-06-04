class Solution {
public:
    int findContentChildren(vector<int>& greed_factors, vector<int>& cookie_sizes) {
        sort(greed_factors.begin(), greed_factors.end());
        sort(cookie_sizes.begin(), cookie_sizes.end());

        int child_idx = 0;
        int cookie_idx = 0;

        while (child_idx < greed_factors.size() && cookie_idx < cookie_sizes.size()) {
            // Give cookie if it satisfies the child's greed
            if (greed_factors[child_idx] <= cookie_sizes[cookie_idx]) {
                child_idx++;
            }
            cookie_idx++;
        }
        return child_idx;
    }
};
