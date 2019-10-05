from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(int(len(candies) / 2), len(set(candies)))


if __name__ == "__main__":
    solution = Solution()
    candies = [1, 1, 2, 2, 3, 3]
    out = solution.distributeCandies(candies)
    print(out)
