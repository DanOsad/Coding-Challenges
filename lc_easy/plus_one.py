#https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for j in str(int(''.join([str(num) for num in digits])) + 1).split() for i in j]

cases = [
    {
        "input": [1,2,3],
        "solution": [1,2,4]
    },
    {
        "input": [4,3,2,1],
        "solution": [4,3,2,2]
    },
    {
        "input": [9],
        "solution": [1,0]
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
        answer = Solution().plusOne(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 