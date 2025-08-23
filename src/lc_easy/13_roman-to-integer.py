# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for index, char in enumerate(s):
            curr_val = roman_map[char]
            if index < len(s) - 1:
                next_val = roman_map[s[index+1]]
                if curr_val < next_val:
                    res -= curr_val
                else:
                    res += curr_val
            else:
                res += curr_val

        return res


cases = [
    {
        'input': "III",
        'solution': 3
    },
    {
        'input': "LVIII",
        'solution': 58
    },
    {
        'input': "MCMXCIV",
        'solution': 1994
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().romanToInt
    }
)
test_suite.run_tests()