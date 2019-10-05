from typing import List
import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = list(string.ascii_lowercase)
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                       "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        dictionary = dict(zip(alphabets, morse_codes))
        morse_code_words = []
        for word in words:
            morse_code_word = []
            for char in word:
                morse_code_word.append(dictionary[char])
            morse_code_words.append(''.join(morse_code_word))
        return(len(set(morse_code_words)))


if __name__ == "__main__":
    solution = Solution()
    words = ["gin", "zen", "gig", "msg"]
    out = solution.uniqueMorseRepresentations(words)
    print(out)
