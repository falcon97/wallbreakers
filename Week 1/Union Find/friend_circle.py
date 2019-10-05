from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        n = len(M)
        parent = list(range(n))
        for i in range(n):
            for j in range(len(M[i])):
                if M[i][j]:
                    union(i, j)
        circle = set(find(i) for i in range(n))
        return len(circle)


if __name__ == "__main__":
    solution = Solution()
    input = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    out = solution.findCircleNum(input)
    print(out)
