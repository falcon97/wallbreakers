class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t))-sum(map(ord, s)))


if __name__ == "__main__":
    solution = Solution()
    a = 'abcd'
    b = 'abcde'
    out = solution.findTheDifference(a, b)
    print(out)
