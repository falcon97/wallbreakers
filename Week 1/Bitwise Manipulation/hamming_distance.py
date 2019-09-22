class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    solution = Solution()
    x, y = 1, 4
    out = solution.hammingDistance(x, y)
    print(out)
