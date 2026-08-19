from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct = [key for key,value in count.items() if value==1]
        print(distinct)
        if len(distinct) >= k:
            return distinct[k-1]
        return ""
