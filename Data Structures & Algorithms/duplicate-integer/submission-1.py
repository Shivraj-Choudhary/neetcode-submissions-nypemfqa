class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for number in nums:
            if number in s:
                return True
            else:
                s.add(number)
        return False
        