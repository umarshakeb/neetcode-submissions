class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_nums = set(nums)
        return not len(nums)==len(check_nums)
         