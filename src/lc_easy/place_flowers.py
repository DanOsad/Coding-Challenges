# 605 https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:        
        bed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) + 1):
            if bed[i-1] == bed[i] == bed[i+1] == 0:
                n -= 1
                bed[i] = 1

            if n <= 0:
                return True
        return False

cases = [
    {
        'input':   [[1,0,0,0,1], 1],
        'solution': True
    },
    {
        'input': [[1,0,0,0,1], 2],
        'solution': False
    },
    {
        'input': [[1,0,0,0,0,1], 2],
        'solution': False
    },
    {
        'input': [[1,0], 1],
        'solution': False
    },
    {
        'input': [[1,0,0,0,1,0,0], 2],
        'solution': True
    },
    {
        'input': [[0,0,0,0,0,1,0,0], 0],
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
        answer = Solution().canPlaceFlowers(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 