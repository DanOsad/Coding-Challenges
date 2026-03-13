# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        vowels = {'a','e','i','o','u'}
        s = list(s)
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i].lower() not in vowels:
                i += 1
            if s[j].lower() not in vowels:
                j -= 1
        return ''.join(s)


cases = [
    {
        'input': 'IceCreAm',
        'solution': 'AceCreIm'
    },
    {
        'input': 'leetcode',
        'solution': 'leotcede'
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().reverseVowels
    }
)
test_suite.run_tests()