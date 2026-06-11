from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for cs, ct in zip(s,t):
            if (cs in count_s and count_s[cs] != ct) or \
                (ct in count_t and count_t[ct] != cs):
                return False
            count_s[cs] = ct
            count_t[ct] = cs
        return True

        