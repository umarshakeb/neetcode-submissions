class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                    three_num = int(num[i])
                    if three_num > max_digit:
                        max_digit = three_num
        if max_digit != -1:
            return str(max_digit)*3
        else:
            return ""



        