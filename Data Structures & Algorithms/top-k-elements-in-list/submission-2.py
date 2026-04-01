class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freqq = [[] for i in range(len(nums) + 1)]
        for num, c in freq.items():
            freqq[c].append(num)
        
        res = []
        for i in range(len(freqq) - 1, 0, -1):
            for num in freqq[i]:
                res.append(num)
                if len(res) == k:
                    return res
