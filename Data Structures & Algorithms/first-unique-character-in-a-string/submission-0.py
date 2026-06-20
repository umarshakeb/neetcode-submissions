class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map.keys():
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        element = [key for key,value in hash_map.items() if hash_map[key]==1]
        return s.index(element[0]) if element else -1

        