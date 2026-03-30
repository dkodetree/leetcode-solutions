class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (!std::isalnum(static_cast<unsigned char>(s[left]))) {
                left++;
            } 
            else if (!std::isalnum(static_cast<unsigned char>(s[right]))) {
                right--;
            } 
            else if (std::tolower(static_cast<unsigned char>(s[left])) != 
                     std::tolower(static_cast<unsigned char>(s[right]))) {
                return false;
            } 
            else {
                left++;
                right--;
            }
        }
        return true;
    }
};
