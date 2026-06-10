class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = (len(nums)*(len(nums)+1))//2
        nums_sum = 0
        for i in nums:
            nums_sum += i
        return actual_sum - nums_sum 

        