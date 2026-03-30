class Solution {
public:
    bool isPalindrome(string s) {
        std::string filtered = "";

        for (char character : s) {
            if (std::isalnum(character)) {
                filtered += std::tolower(character);
            }
        }

        return std::equal(filtered.begin(), filtered.end(), filtered.rbegin());
    }
};
