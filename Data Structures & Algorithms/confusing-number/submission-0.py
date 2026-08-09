class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        new_num = ""
        mapping = {
            "0" : 0,
            "1" : 1,
            "6" : 9,
            "8" : 8,
            "9" : 6
        }
        for i in range(len(n)-1,-1,-1):
            if n[i] in mapping.keys():
                new_num += str(mapping[n[i]])
            else:
                return False
        if int(new_num) == int(n):
            return False
        return True
            


        