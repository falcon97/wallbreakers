from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_elements = [element for element in A if element % 2 == 0]
        odd_elements = [element for element in A if element % 2 != 0]
        return even_elements + odd_elements


if __name__ == "__main__":
    solution = Solution()
    test_case = [3, 1, 2, 4]
    out = solution.sortArrayByParity(test_case)
    print(out)
