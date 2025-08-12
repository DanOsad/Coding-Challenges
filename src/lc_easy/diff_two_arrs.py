# 2215 https://leetcode.com/problems/find-the-difference-of-two-arrays

class Solution:
    def findDifference(self, nums1: list, nums2: list) -> list:
        s1 = set(nums1)
        s2 = set(nums2)
        return [ list(s1 - s2), list(s2 - s1) ]


cases = [
    {
        'input':   [[1,2,3],[2,4,6]],
        'solution': [[1,3],[4,6]]
    },
    {
        'input': [[1,2,3,3], [1,1,2,2]],
        'solution': [[3],[]]
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
        answer = Solution().findDifference(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 