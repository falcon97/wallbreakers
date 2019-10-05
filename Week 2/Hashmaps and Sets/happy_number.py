class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n not in sums:
            sums.add(n)
            n = sum([int(i)**2 for i in str(n)])
        if 1 in sums:
            return True


if __name__ == "__main__":
    solution = Solution()
    num = 19
    out = solution.isHappy(num)
    print(out)
