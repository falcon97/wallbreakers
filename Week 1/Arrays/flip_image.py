from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [l[::-1] for l in A]
        for l in A:
            for i in range(len(l)):
                l[i] = int(not l[i])
        return A


if __name__ == "__main__":
    solution = Solution()
    test_case = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    out = solution.flipAndInvertImage(test_case)
    print(out)
