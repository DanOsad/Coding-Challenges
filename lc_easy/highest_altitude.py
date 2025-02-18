# https://leetcode.com/problems/find-the-highest-altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution:
    def largestAltitude(self, gain: list) -> int:
        highest_point = 0
        current = 0
        for n in range(len(gain)):
            current += gain[n]
            if current > highest_point:
                highest_point = current
        return highest_point
    
cases = [
    {
        'input':  [-5,1,5,0,-7],
        'solution': 1
    },
    {
        'input': [-4,-3,-2,-1,4,3,2],
        'solution': 0
    },
    {
        'input': [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81],
        'solution': 781
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
        answer = Solution().largestAltitude(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 