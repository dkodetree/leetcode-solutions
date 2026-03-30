class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> bracketMapping = new HashMap<>(); // close -> open
        bracketMapping.put(')', '(');
        bracketMapping.put('}', '{');
        bracketMapping.put(']', '[');

        Stack<Character> stack = new Stack<>();
        
        for (char ele : s.toCharArray()) {
            if (bracketMapping.containsKey(ele)) {  // close
                if (stack.isEmpty() || stack.pop() != bracketMapping.get(ele)) {
                    return false;
                }
            }
            else {      // Open
                stack.push(ele);
            }
        }
        return stack.isEmpty();
    }
}
