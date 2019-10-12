from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_list_unbanned = [w for w in re.findall(
            '\w+', paragraph.lower()) if w not in banned]
        return collections.Counter(words_list_unbanned).most_common(1)[0][0]


if __name__ == "__main__":
    solution = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    out = solution.mostCommonWord(paragraph, banned)
    print(out)
