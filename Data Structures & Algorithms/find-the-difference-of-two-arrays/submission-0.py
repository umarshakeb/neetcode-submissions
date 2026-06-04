class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = []
        list2 = []
        for element in set(nums1):
            if element not in set(nums2):
                list1.append(element)
        for element in set(nums2):
            if element not in set(nums1):
                list2.append(element)
        new_list = [list1,list2]
        return new_list

        