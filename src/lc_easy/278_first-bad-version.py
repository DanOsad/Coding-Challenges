# https://leetcode.com/problems/first-bad-version/
class Solution:
        # The isBadVersion API is already defined for you.
        # def isBadVersion(version: int) -> bool:

    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n + 1

        while left < right:
            middle = (left + right) // 2
            if (isBadVersion(middle)):
                right = middle
            else:
                left = middle + 1

        return left

cases = [
    {
        'input': (5, 4),
        'solution': 4
    },
    {
        'input': (1, 1),
        'solution': 1
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().isBadVersion
    }
)
test_suite.run_tests()