#https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0: return False
        bracket_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        opening_brackets = bracket_map.values()
        bracket_stack = []
        for bracket in s:
            if bracket in opening_brackets:
                bracket_stack.append(bracket)
            else:
                if not bracket_stack:
                    return False
                if bracket_stack[-1] == bracket_map[bracket]:
                    bracket_stack.pop()
                else:
                    return False
        return len(bracket_stack) == 0
        

cases = [
    {
        'name': 'case1',
        'str':  "()",
        'solution': True
    },
    {
        'name': 'case2',
        'str': "()[]{}",
        'solution': True
    },
    {
        'name': 'case3',
        'str': "(]",
        'solution': False
    },
    {
        'name': 'case4',
        'str': "((",
        'solution': False
    },
    {
        'name': 'case5',
        'str': "){",
        'solution': False
    },
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def test():
    for case in cases:
        print(f'Testing {case["name"]}')
        s = Solution()
        answer = s.isValid(case['str'])
        is_correct = answer == case['solution']
        print(f'Expected {case["solution"]}, got {answer} = {is_correct} | {passed() if is_correct else failed()}')

test()