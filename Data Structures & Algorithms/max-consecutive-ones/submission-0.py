class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        compare = 0
        count = 0
        for i in nums:
            if i==1:
                count+=1
            if count> compare:
                compare = count
            if i == 0:
                count = 0
        return compare    


        