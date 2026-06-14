class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return [item for item in range(1,len(nums)+1) if item not in nums]

        