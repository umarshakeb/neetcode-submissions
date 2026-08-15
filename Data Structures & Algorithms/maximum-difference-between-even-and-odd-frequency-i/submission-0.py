from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        f = Counter(s)
        odd_f = [val for val in f.values() if val%2 != 0]
        even_f = [val for val in f.values() if val%2 == 0]
        return max(odd_f) - min(even_f)