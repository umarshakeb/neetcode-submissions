class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_of_index = []
        for i in nums1:
            if i in nums2:
                list_of_index.append(nums2.index(i))
        return list_of_index
        