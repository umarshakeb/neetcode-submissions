from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        left, right = "", ""
        total = 0
        for i in range(len(s) - 1):
            left = s[:i+1]
            right = s[i+1:]
            left_sum  = Counter(left)
            right_sum = Counter(right)
            total_sum = left_sum['0'] + right_sum['1']
            left_sum.clear()
            right_sum.clear()
            if total_sum > total:
                total = total_sum
        return total


        