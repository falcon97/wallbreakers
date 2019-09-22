from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            num = num ^ i
        return num


if __name__ == "__main__":
    solution = Solution()
    input = [2, 2, 1]
    out = solution.singleNumber(input)
    print(out)
