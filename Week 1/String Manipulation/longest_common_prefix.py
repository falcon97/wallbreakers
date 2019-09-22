from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_list = list(zip(*strs))
        common_prefix = ''
        for letters in common_list:
            if len(set(letters)) == 1:
                common_prefix += letters[0]
            else:
                break
        return common_prefix


if __name__ == "__main__":
    solution = Solution()
    input = ["flower", "flow", "flight"]
    out = solution.longestCommonPrefix(input)
    print(out)
