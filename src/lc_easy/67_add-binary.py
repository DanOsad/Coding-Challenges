# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0

        a_rev, b_rev = a[::-1], b[::-1]

        for i in range(max(len(a_rev), len(b_rev))):
            digit_a = int(a_rev[i]) if i < len(a_rev) else 0
            digit_b = int(b_rev[i]) if i < len(b_rev) else 0

            total = digit_a + digit_b + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2
        if carry > 0:
            res = "1" + res

        return res


cases = [
    {
        'input': ["11", "1"],
        'solution': "100"
    },
    {
        'input': ["1010", "1011"],
        'solution': "10101"
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().addBinary
    }
)
test_suite.run_tests()