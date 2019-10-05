from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot
            self.count -= 1

        if len(grid) == 0:
            return 0
        r = len(grid)
        c = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(r) for j in range(c))
        parent = [i for i in range(r*c)]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    continue
                index = i*c + j
                if j < c-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < r-1 and grid[i+1][j] == '1':
                    union(index, index+c)
        return self.count


if __name__ == "__main__":
    solution = Solution()
    input = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
    out = solution.numIslands(input)
    print(out)
