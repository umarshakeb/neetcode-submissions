class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums[i+1:]:
                position = nums.index(remainder, i + 1)
                break
        return [i, position] if i<position else [position,i]
