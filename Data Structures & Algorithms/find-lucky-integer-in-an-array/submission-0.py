class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_num = {}
        for i in arr:
            if i in count_num.keys():
                count_num[i] +=1
            else:
                count_num[i] = 1
        result = -1
        for key, value in count_num.items():
            if key == value:
                result = max(key, result)
        return result
        