from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    out = solution.intersection(nums1, nums2)
    print(out)
