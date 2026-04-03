class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num,0) + 1);
        }
        List<int[]> list = new ArrayList<>();
        map.forEach((number, frequency) -> list.add( new int[] {frequency, number}));
        list.sort((a,b) -> b[0] - a[0]);

        int[] arr = new int[k];
        for (int i = 0; i<k; i++) {
            arr[i] = list.get(i)[1];
        }
        return arr;
    }
}
