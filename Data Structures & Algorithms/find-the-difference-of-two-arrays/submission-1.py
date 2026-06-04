class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        for element in set(nums1):
            if element not in set(nums2):
                answer[0].append(element)
        for element in set(nums2):
            if element not in set(nums1):
                answer[1].append(element)
        return answer

        