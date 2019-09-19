from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(l) for l in zip(*A)]


if __name__ == "__main__":
    solution = Solution()
    test_case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    out = solution.transpose(test_case)
    print(out)
