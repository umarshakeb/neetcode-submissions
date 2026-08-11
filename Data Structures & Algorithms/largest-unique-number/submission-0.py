from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        list_nums = Counter(nums)
        keys = [key for key,val in list_nums.items() if val==1]
        if keys:
            return max(keys)
        else:
            return -1



