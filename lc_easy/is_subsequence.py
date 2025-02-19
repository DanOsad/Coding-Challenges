# https://leetcode.com/problems/is-subsequence
# two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # track s
        j = 0 # track t        

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
            j+=1

        return i == len(s)

cases = [
    {
        'input':  ["abc", "ahbgdc"],
        'solution': True
    },
    {
        'input': ["axc", "ahbgdc"],
        'solution': False
    },
    {
        'input': ["", "ahbgdc"],
        'solution': True
    },
    {
        'input': ["b", "c"],
        'solution': False
    },
    {
        'input': ["abc", ""],
        'solution': False
    },
    {
        'input': ["bb", "ahbgdc"],
        'solution': False
    },
    {
        'input': ["b", "abc"],
        'solution': True
    },
    {
        'input': ["", ""],
        'solution': True
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
        answer = Solution().isSubsequence(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test()