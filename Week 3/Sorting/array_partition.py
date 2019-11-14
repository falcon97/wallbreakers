from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 2]
    out = solution.arrayPairSum(nums)
    print(out)
