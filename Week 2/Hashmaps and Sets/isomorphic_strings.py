class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = "add"
    out = solution.isIsomorphic(s, t)
    print(out)
