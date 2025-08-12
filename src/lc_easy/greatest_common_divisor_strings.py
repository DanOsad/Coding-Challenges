#1071 https://leetcode.com/problems/greatest-common-divisor-of-strings

import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str2 + str1) != (str1 + str2):
            return ""
        else:
            gcd_val = math.gcd(len(str1), len(str2))
            return str1[0:gcd_val]



cases = [
    {
        'input':   ["ABCABC", "ABC"],
        'solution': "ABC"
    },
    {
        'input': ["ABABAB", "ABAB"],
        'solution': "AB"
    },
    {
        'input': ["LEET", "CODE"],
        'solution': ""
    },
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def pass_fail(is_correct: bool):
    return passed() if is_correct else failed()

def test():
    for i, case in enumerate(cases, 1):
        answer = Solution().gcdOfStrings(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 