class Solution:
    def titleToNumber(self, s: str) -> int:
        col_num = 0
        for ch in s:
            col_num = col_num * 26 + ord(ch) - 64
        return col_num


if __name__ == "__main__":
    solution = Solution()
    input = 'AB'
    out = solution.titleToNumber(input)
    print(out)
