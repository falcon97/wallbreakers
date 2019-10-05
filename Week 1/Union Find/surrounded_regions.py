from typing import List


class Solution:

    def traverse(self, board, parents, r, c, pr, pc):
        if (r, c) in parents or r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1 or board[r][c] != 'O':
            return
        else:
            parentCurr = self.find((r, c), parents)
            parentPrev = self.find((pr, pc), parents)
            if parentCurr != parentPrev:
                parents[parentCurr] = parentPrev
            self.traverse(board, parents, r+1, c, r, c)
            self.traverse(board, parents, r-1, c, r, c)
            self.traverse(board, parents, r, c+1, r, c)
            self.traverse(board, parents, r, c-1, r, c)

    def find(self, node, parents):
        if node not in parents:
            parents[node] = node
            return node
        if parents[node] != node:
            parents[node] = self.find(parents[node], parents)
        return parents[node]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        parents = {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    self.traverse(board, parents, r, c, -1, -1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'O' and parents.get((r, c)) != (-1, -1):
                    board[r][c] = 'X'


if __name__ == "__main__":
    solution = Solution()
    input = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    solution.solve(input)
    print(input)
