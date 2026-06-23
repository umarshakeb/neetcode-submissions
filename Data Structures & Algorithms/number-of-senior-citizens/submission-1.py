class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age_list = []
        count = 0
        for word in details:
            cleaned = "".join([" " if char in "MFO" else char for char in word])
            cleaned = cleaned.split(" ")[1]
            age_list.append(cleaned[:2])
        for i in age_list:
            if int(i)>60:
                count+=1
        return count
