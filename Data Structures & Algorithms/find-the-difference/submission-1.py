from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        diff = count_t-count_s
        diff = list(diff.keys())
        return diff[0]
        