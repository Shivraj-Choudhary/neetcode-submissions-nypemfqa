class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        s = {}
        for num in nums:
            s[num] = s.get(num, 0) + 1
        sorted_keys = sorted(s, key = lambda x:s[x], reverse = True)
        return sorted_keys[:k]