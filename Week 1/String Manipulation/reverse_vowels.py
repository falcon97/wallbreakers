class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        v_indices = []
        v_chars = []
        s = list(s)
        for i, ch in enumerate(s):
            if ch in vowels:
                v_indices.append(i)
                v_chars.append(ch)
        for i in v_indices:
            s[i] = v_chars.pop()
        return ''.join(s)


if __name__ == "__main__":
    solution = Solution()
    input = 'hello'
    out = solution.reverseVowels(input)
    print(out)
