class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)) and len(pattern) == len(s)


if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    out = solution.wordPattern(pattern, str)
    print(out)
