from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


if __name__ == "__main__":
    solution = Solution()
    input = ["h", "e", "l", "l", "o"]
    solution.reverseString(input)
    print(input)
