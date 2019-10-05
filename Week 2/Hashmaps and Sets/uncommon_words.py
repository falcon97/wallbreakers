from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        all_words = list((A+" "+B).split(" "))
        return [word for word in all_words if all_words.count(word) == 1]


if __name__ == "__main__":
    solution = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"
    out = solution.uncommonFromSentences(A, B)
    print(out)
