class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if len(word) <= 1:
            return 1
        t = keyboard.index(word[0])
        present_idx = keyboard.index(word[0])
        for i in range(1, len(word)):
            idx = keyboard.index(word[i])
            step = abs(present_idx-idx)
            present_idx = idx
            t += step
        return t