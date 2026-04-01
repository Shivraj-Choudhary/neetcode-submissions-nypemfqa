class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f = [0] * 26
        for i in range(len(s)):
            si = ord(s[i]) - ord('a')
            ti = ord(t[i]) - ord('a')
            f[si] += 1
            f[ti] -= 1
        for i in f:
            if i != 0:
                return False
        return True