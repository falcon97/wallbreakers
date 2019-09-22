class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    solution = Solution()
    s = 'anagram'
    t = 'nagaram'
    out = solution.isAnagram(s, t)
    print(out)
