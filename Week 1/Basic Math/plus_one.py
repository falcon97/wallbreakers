from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join(str(digit) for digit in digits)
        return [int(digit) for digit in str(int(num_str) + 1)]


if __name__ == "__main__":
    solution = Solution()
    input = [1, 2, 3]
    out = solution.plusOne(input)
    print(out)
