class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        n = len(nums)
        res = [0] * n
        for num in nums:
            if num:
                product *= num
            else:
                zeros += 1

        if zeros > 1:
            return res
        elif zeros == 1:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = product
            return res
        else:
            for i in range(n):
                res[i] = product // nums[i]
            return res