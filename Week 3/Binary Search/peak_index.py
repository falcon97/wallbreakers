from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    solution = Solution()
    test_case = [0, 1, 0]
    out = solution.peakIndexInMountainArray(test_case)
    print(out)
