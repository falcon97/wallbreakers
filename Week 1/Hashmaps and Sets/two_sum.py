from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i, i + 1 + nums[i + 1:].index(target - nums[i])]


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    out = solution.twoSum(nums, target)
    print(out)
