# https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0
    def guess(self, num: int) -> int:
        target = 2
        if num == target:
            return 0
        elif num > target:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        lo = 0
        hi = n

        while lo <= hi:
            mid = (hi + lo) // 2
            guessed = self.guess(mid)
            if guessed == 0:
                return mid
            if guessed > 0:
                lo = mid + 1
            else:
                hi = mid
            if hi == lo:
                return lo


cases = [
    {
        'input': 10,
        'solution': 6
    },
    {
        'input': 2,
        'solution': 2
    },
    {
        'input': 1,
        'solution': 1
    },
    {
        'input': 2,
        'solution': 1
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().guessNumber
    }
)
test_suite.run_tests()