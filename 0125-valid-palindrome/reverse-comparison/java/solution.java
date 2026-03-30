class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder filtered = new StringBuilder();

        for (char ele : s.toCharArray()) {
            if (Character.isLetterOrDigit(ele)) {
                filtered.append(Character.toLowerCase(ele));
            }
        }
        
        return filtered.toString().equals(filtered.reverse().toString());
    }
}
