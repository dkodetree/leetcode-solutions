class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> bracketMap = new HashMap<>(); // close -> open
        bracketMap.put(')', '(');
        bracketMap.put('}', '{');
        bracketMap.put(']', '[');

        Stack<Character> openBracketStack = new Stack<>();
        
        for (char ele : s.toCharArray()) {
            if (bracketMap.containsKey(ele)) {  // close
                if (openBracketStack.isEmpty() || openBracketStack.pop() != bracketMap.get(ele)) {
                    return false;
                }
            }
            else {      // open
                openBracketStack.push(ele);
            }
        }
        return openBracketStack.isEmpty();
    }
}
