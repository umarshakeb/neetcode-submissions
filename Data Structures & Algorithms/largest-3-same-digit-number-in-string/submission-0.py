class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = -1
        s = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                    s = num[i]
                    three_num = int(s)
                    if three_num > max_digit:
                        max_digit = three_num
                    s = ""
        if max_digit != -1:
            return str(max_digit)*3
        else:
            return ""



        