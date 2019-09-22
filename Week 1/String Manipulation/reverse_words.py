class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        l = [s[::-1] for s in l]
        rev = " ".join(l)
        return rev


if __name__ == "__main__":
    solution = Solution()
    input = "Let's take LeetCode contest"
    out = solution.reverseWords(input)
    print(out)
