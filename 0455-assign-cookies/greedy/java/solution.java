class Solution {
    public int findContentChildren(int[] greedFactors, int[] cookieSizes) {
        Arrays.sort(greedFactors);
        Arrays.sort(cookieSizes);
        
        int childIdx = 0;
        int cookieIdx = 0;

        while (childIdx < greedFactors.length && cookieIdx < cookieSizes.length) {
            // Give cookie if it satisfies the child's greed
            if (greedFactors[childIdx] <= cookieSizes[cookieIdx]) {
                childIdx++;
            }
            cookieIdx++;
        }
        return childIdx;
    }
}
