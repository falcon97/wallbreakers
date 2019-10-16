class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x * x, n / 2)


if __name__ == "__main__":
    solution = Solution()
    x, n = (2, 10)
    out = solution.myPow(x, n)
    print(out)
