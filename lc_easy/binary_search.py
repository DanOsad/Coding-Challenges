# https://leetcode.com/problems/binary-search
# nums is sorted ASCENDING
# O(log(n)) time complexity required
import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        
        if len(nums) <= 1 and nums[lo] == target:
            return lo

        while hi > lo:
            m = math.floor(lo + (hi-lo) / 2)
            print('new_m', m)
            if nums[m] == target:
                return m
            if target > nums[m]:
                lo = m + 1
            else:
                hi = m
            
            if hi == lo and nums[lo] == target:
                return lo
        return -1


cases = [
    {
        'input':  [[-1,0,3,5,9,12], 9],
        'solution': 4
    },
    {
        'input': [[-1,0,3,5,9,12], 2],
        'solution': -1
    },
    {
        'input': [[5], 5],
        'solution': 0
    },
    {
        'input': [[2,5], 5],
        'solution': 1
    }
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def pass_fail(is_correct: bool):
    return passed() if is_correct else failed()

def test():
    for i, case in enumerate(cases, 1):
        answer = Solution().search(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 