# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        longest_substring = 0
        while j < len(s) + 1:
            current_substring = s[i:j+1]
            if len(current_substring) == len(set(current_substring)):
                if len(current_substring) > longest_substring:
                    longest_substring = len(current_substring)
                j += 1
            else:
                i += 1
        return longest_substring


cases = [
    {
        'input': 'abcabcbb',
        'solution': 3
    },
    {
        'input': 'bbbbb',
        'solution': 1
    },
    {
        'input': 'pwwkew',
        'solution': 3
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().lengthOfLongestSubstring
    }
)
test_suite.run_tests()