from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index, cookie = 0, 0
        while g_index < len(g) and cookie < len(s):
            if s[cookie] >= g[g_index]:
                g_index += 1
            cookie += 1
        return g_index


if __name__ == "__main__":
    solution = Solution()
    g = [1, 2, 3]
    s = [1, 1]
    out = solution.findContentChildren(g, s)
    print(out)
