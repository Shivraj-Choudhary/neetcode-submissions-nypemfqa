class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        store = set(nums)

        for num in nums:
            streak = 0
            while num + 1 in store:
                streak += 1
                num += 1

            if streak > res:
                res = streak
        return res + 1