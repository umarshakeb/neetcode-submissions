class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = []
        for i in nums1:
            idx = nums2.index(i)
            found = -1
            for j in range(idx+1, len(nums2)):
                if nums2[j]>i:
                    found = nums2[j]
                    break
            next_greater.append(found)
        return next_greater
        