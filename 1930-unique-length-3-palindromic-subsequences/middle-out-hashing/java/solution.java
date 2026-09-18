class Solution {
    public int countPalindromicSubsequence(String s) {
        Set<Integer> res = new HashSet<>();
        Set<Character> left = new HashSet<>();
        int[] right = new int[26]; 
        for (int idx = 0; idx < s.length(); idx++) {
            right[s.charAt(idx) - 'a']++;
        }

        for (int idx = 0; idx < s.length(); idx++) {   // at most n
            char mid = s.charAt(idx);
            int midIdx = mid - 'a';
            right[midIdx]--;     

            for (char outer : left) {            // at most 26
                int outerIdx = outer - 'a';
                if (right[outerIdx] > 0) {
                    res.add(outerIdx * 26 + midIdx); // encoding (outer, mid) as an unique integer
                }
            }
            left.add(mid);
        }
        return res.size();
    }
}
