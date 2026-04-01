class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)
        for num in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if num == j:
                    continue
                else:
                    prod *= nums[j]
            product[num] = prod
        return product

