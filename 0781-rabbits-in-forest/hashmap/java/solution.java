class Solution {
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> ansFreqMap = new HashMap<>();
        for (int ans : answers) {
            ansFreqMap.put(ans, ansFreqMap.getOrDefault(ans, 0) + 1);
        }

        int totalRabbits = 0;
        for (var entry : ansFreqMap.entrySet()) {
            int ans = entry.getKey();
            int freq = entry.getValue();
            int groupSize = ans + 1;
            int numGroups = (int) Math.ceil((double) freq / groupSize);
            totalRabbits += numGroups * groupSize;
        }
        return totalRabbits;
    }
}
