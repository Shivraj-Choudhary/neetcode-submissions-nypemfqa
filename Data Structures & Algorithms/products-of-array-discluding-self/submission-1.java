class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] num = new int[nums.length];
        for (int i = 0; i<nums.length; i++) {
            int res = 1;
            for (int j = 0; j<nums.length; j++) {
                if (j == i) {
                    continue;
                }
                res *= nums[j];
            }
            num[i] = res;
        }
        return num;
    }
}  
