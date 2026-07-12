import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # for _ in range(k):
        #     element = max(gifts)
        #     idx = gifts.index(element)
        #     gifts[idx] = math.isqrt(element)
        # return sum(gifts)
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            new_val = math.isqrt(largest)
            heapq.heappush(max_heap,-new_val)
        return -sum(max_heap)




        