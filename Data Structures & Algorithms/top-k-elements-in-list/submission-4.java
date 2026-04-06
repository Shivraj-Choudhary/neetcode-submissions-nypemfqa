class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num,0) + 1);
        }
        PriorityQueue<int[]> mheap = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        for (Map.Entry<Integer, Integer> entry: map.entrySet()) {
            mheap.offer(new int[]{entry.getValue(), entry.getKey()});
            if (mheap.size() > k) {
                mheap.poll();
            }
        }
        int[] arr = new int[k];
        for (int i = 0; i < k; i++) {
            arr[i] = mheap.poll()[1];
        }
        return arr;
    }
}
