class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list= {}
        response = []
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in new_list:
                new_list[key] = [i]
            else:
                new_list[key].append(i)
        for key in new_list:
            values = new_list[key]
            response.append([strs[k] for k in values])
        return response


        