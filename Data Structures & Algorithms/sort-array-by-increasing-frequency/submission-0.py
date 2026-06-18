class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict_of_nums = {}
        nums_list = []
        for i in range(len(nums)):
            if nums[i] in dict_of_nums.keys():
                dict_of_nums[nums[i]] += 1
            else:
                dict_of_nums[nums[i]] = 1
        sorted_dict = sorted(dict_of_nums.items(), key= lambda x:(x[1], -x[0]))
        for key, value in sorted_dict:
            nums_list.extend([key]*value)
        return nums_list



        