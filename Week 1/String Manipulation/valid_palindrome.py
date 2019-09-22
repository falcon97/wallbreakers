class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(ch for ch in s if ch.isalnum()).lower()
        return new_str == new_str[::-1]


if __name__ == "__main__":
    solution = Solution()
    input = "A man, a plan, a canal: Panama"
    out = solution.isPalindrome(input)
    print(out)
