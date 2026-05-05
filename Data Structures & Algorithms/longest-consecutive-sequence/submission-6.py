class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        store = set(nums)
        streak = 0
        for num in nums:
            # curr = num
            if num-1 not in store:
                curr = num
                streak = 1
                while curr + 1 in store:
                    curr += 1
                    streak += 1
                res = max(streak, res)
        return res