from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_freq = Counter(words[0])
        for word in words[1:]:
            new_freq = Counter(word)
            for char in list(word_freq.keys()):
                if char in new_freq:
                    word_freq[char] = min(word_freq[char],new_freq[char])
                else:
                    del word_freq[char]

        result = []
        for char, count in word_freq.items():
            result.extend([char]*count)
        return result



