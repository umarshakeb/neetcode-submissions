class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list = []
        for i in range(len(operations)):
            if operations[i] == "+":
                new_list.append(new_list[-1] + new_list[-2])
            elif operations[i] == "D":
                new_list.append(new_list[-1]*2)
            elif operations[i] == "C":
                new_list.pop()
            else:
                new_list.append(int(operations[i]))
        return sum(new_list)