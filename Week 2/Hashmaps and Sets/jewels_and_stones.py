class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for ch in J:
            c = c+S.count(ch)
        return c


if __name__ == "__main__":
    solution = Solution()
    J = "aA"
    S = "aAAbbbb"
    out = solution.numJewelsInStones(J, S)
    print(out)
