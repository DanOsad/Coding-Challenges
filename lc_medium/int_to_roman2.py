#12 https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = [
            (1000 ,"M"),
            (900 ,"CM"),
            (500 ,"D"),
            (400 ,"CD"),
            (100 ,"C"),
            (90, "XC"),
            (50 ,"L"),
            (40, "XL"),
            (10 ,"X"),
            (9, "IX"),
            (5 ,"V"),
            (4, "IV"),
            (1 ,"I"),
        ]

        ret = ""
        i = 0

        while num > 0:
            for n, r in roman_map:
                if num >= n:
                    num -= n
                    ret += r
                    break
            i += 1
        return ret

    
cases = [ 
    {
        'input':  3749,
        'solution': "MMMDCCXLIX"
    },
    {
        'input': 58,
        'solution': "LVIII"
    },
    {
        'input': 1994,
        'solution': "MCMXCIV"
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
        answer = Solution().intToRoman(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 