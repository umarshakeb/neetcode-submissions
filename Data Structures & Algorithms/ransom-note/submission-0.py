from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_dict = Counter(ransomNote)
        mag_dict = Counter(magazine)
        return rn_dict <= mag_dict

        