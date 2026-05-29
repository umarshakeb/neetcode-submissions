class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        prefix = strs[0]
        for i in range(1, len(strs)):
            if strs[i] == "":
                return ""
            for j in range(min(len(prefix),len(strs[i]))):
                if prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = prefix[:j]
                    break
        return prefix


        