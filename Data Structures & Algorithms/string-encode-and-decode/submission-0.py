class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for num in strs:
            res += str(len(num)) + "_" + num
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res