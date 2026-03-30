class Solution {
    public boolean isValid(String s) {
        String curStr = s;
        int prevLength;

        do {
            prevLength = curStr.length();
            curStr = curStr.replace("()", "")
                           .replace("{}", "")
                           .replace("[]", "");
        } while (curStr.length() < prevLength);

        return curStr.isEmpty();
    }
}
