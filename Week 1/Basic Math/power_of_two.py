class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while num < n:
            num *= 2
        return num == n


if __name__ == "__main__":
    solution = Solution()
    input = 16
    out = solution.isPowerOfTwo(input)
    print(out)
