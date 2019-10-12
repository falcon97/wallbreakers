class Solution:
    def firstUniqChar(self, s: str) -> int:
        idxs = []
        for c in set(s):
            if s.count(c) == 1:
                idxs.append(s.index(c))
        if len(idxs) > 0:
            return min(idxs)
        else:
            return -1


if __name__ == "__main__":
    solution = Solution()
    test_case = 'leetcode'
    out = solution.firstUniqChar(test_case)
    print(out)
