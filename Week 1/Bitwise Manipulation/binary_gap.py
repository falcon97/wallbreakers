class Solution:
    def binaryGap(self, N: int) -> int:
        start = 0
        gap = 0
        for i, ch in enumerate(bin(N)[2:]):
            if ch == '1':
                gap = max(gap, i-start)
                start = i
        return gap


if __name__ == "__main__":
    solution = Solution()
    input = 22
    out = solution.binaryGap(input)
    print(out)
