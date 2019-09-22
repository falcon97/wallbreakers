class Solution:
    def findComplement(self, num: int) -> int:
        complement = [str(int(not int(d))) for d in list(bin(num)[2:])]
        return int(''.join(complement), 2)


if __name__ == "__main__":
    solution = Solution()
    input = 5
    out = solution.findComplement(input)
    print(out)
