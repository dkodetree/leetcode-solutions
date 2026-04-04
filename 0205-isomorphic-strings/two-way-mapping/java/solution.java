class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Character> sToTMapping = new HashMap<>();
        HashMap<Character, Character> tToSMapping = new HashMap<>();

        for (int idx = 0; idx < s.length(); idx++) {
            char char1 = s.charAt(idx);
            char char2 = t.charAt(idx);
            
            if (sToTMapping.containsKey(char1) && sToTMapping.get(char1) != char2) {
                return false;
            }
            
            if (tToSMapping.containsKey(char2) && tToSMapping.get(char2) != char1) {
                return false;
            }

            sToTMapping.put(char1, char2);
            tToSMapping.put(char2, char1);
        }
        return true;
    }
}
