#1431 https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        mc = max(candies)
        ret = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mc:
                ret.append(True)
            else:
                ret.append(False)

        return ret
    
cases = [
    {
        'input':  [[2,3,5,1,3], 3],
        'solution': [True,True,True,False,True]
    },
    {
        'input':  [[4,2,1,1,2], 1],
        'solution': [True,False,False,False,False]
    },
    {
        'input':  [[12,1,12], 10],
        'solution': [True,False,True]
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
        answer = Solution().kidsWithCandies(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 