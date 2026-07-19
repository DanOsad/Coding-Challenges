# https://leetcode.com/problems/first-bad-version/
class Solution:
        # The isBadVersion API is already defined for you.
        # def isBadVersion(version: int) -> bool:

    def firstBadVersion(self, n: int) -> int:


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