class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_n = n*(n+1)//2
        missing = sum_n - sum(set(nums))
        duplicate = sum(nums) - (sum_n-missing)
        return [duplicate,missing]



        