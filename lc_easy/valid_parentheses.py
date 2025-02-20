# 20 https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        r = []
        for b in s:
            if b in braces:
                r.append(b)
            elif len(r) >= 1:    
                if braces[r[-1]] == b:
                    r.pop()
                else:
                    return False
            else:
                return False

        return len(r) == 0
    
cases = [ 
    {
        'input':  "([])",
        'solution': True
    },
    {
        'input': "]",
        'solution': False
    },
    {
        'input': "(])",
        'solution': False
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
        answer = Solution().isValid(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 