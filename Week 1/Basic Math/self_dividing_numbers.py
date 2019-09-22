from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check_self_divide(num):
            digits = [int(digit) for digit in str(num)]
            if 0 in digits:
                return False
            else:
                for digit in digits:
                    if num % digit == 0 and digit != 0:
                        pass
                    else:
                        return False
            return True
        output_list = []
        for i in range(left, right+1):
            if check_self_divide(i):
                output_list.append(i)
        return output_list


if __name__ == "__main__":
    solution = Solution()
    left, right = 1, 22
    out = solution.selfDividingNumbers(left, right)
    print(out)
