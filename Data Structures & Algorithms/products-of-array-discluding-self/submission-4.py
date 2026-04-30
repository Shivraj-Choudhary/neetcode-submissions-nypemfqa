class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prev = suff = 1
        for i in range(n):
            res[i] = prev
            prev *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        return res