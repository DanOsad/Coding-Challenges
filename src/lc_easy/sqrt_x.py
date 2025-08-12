# https://leetcode.com/problems/sqrtx/

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0
        while left <= right:
            middle = left + ((right - left) // 2)
            square = middle ** 2
            if square > x:
                right = middle - 1
            elif square < x:
                result = middle
                left = middle + 1
            else:
                return middle
        return result

cases = [
    {
        'input':  4,
        'solution': 2
    },
    {
        'input': 8,
        'solution': 2
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().mySqrt
    }
)

test_suite.run_tests()