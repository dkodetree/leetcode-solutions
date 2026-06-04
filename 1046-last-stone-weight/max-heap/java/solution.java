class Solution {
    public int lastStoneWeight(int[] stones) {
        // Java's PriorityQueue is min-heap by default. Passing Collections.reverseOrder() turns it into max-heap.
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int stone : stones) {
            maxHeap.offer(stone);
        }

        while (maxHeap.size() > 1) {
            int firstStone = maxHeap.poll();
            int secondStone = maxHeap.poll();
            if (firstStone != secondStone) {
                maxHeap.add(firstStone - secondStone);
            }
        }
        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
