# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        queue = []
        for c in s:
            queue.append(c)
            if len(queue) >= 2:
                last_item = queue[-1]
                second_last_item = queue[-2]
                if (second_last_item in pairs) and (last_item == pairs[second_last_item]):
                    queue.pop()
                    queue.pop()

        return len(queue) == 0
            



cases = [
    {
        'input': '()',
        'solution': True
    },
    {
        'input': '()[]{}',
        'solution': True
    },
    {
        'input': '(]',
        'solution': False
    },
    {
        'input': '([)]',
        'solution': False
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().isValid
    }
)
test_suite.run_tests()