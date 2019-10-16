from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives > 0:
                tens += 1
                fives -= 1
            elif bill == 20 and fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif bill == 20 and fives > 3:
                fives -= 3
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    bills = [5, 5, 5, 10, 20]
    out = solution.lemonadeChange(bills)
    print(out)
