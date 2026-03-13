# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split()
        rev = split[::-1]
        return ' '.join(rev)

cases = [
    {
        'input': 'the sky is blue',
        'solution': 'blue is sky the'
    },
    {
        'input': '  hello world  ',
        'solution': 'world hello'
    },
    {
        'input': 'a good   example',
        'solution': 'example good a'
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().reverseWords
    }
)
test_suite.run_tests()