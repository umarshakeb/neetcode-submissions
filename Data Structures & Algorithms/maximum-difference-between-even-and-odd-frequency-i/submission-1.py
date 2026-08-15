from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq_s = Counter(s)
        odd_freq = [val for val in freq_s.values() if val%2 != 0]
        even_freq = [val for val in freq_s.values() if val%2 == 0]
        return max(odd_freq) - min(even_freq)