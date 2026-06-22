class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = len(s.rstrip().split(" ")[-1])
        return word_list
        