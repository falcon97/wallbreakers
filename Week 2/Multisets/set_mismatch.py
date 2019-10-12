from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        t = sum(nums)-sum(set(nums))
        n = len(nums)
        not_occured = n*(n+1)//2-sum(set(nums))
        return [t, not_occured]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2, 4]
    out = solution.findErrorNums(nums)
    print(out)
