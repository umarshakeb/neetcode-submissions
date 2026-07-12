import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            element = max(gifts)
            idx = gifts.index(element)
            gifts[idx] = math.isqrt(element)
        return sum(gifts)


        