# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500,
            "M": 1000
        }
        total = 0
        for i, char in enumerate(s):
            curr_val = roman_map[char]
            if i < len(s) - 1:
                next_val = roman_map[s[i+1]]
                if next_val > curr_val:
                    total -= curr_val
                else:
                    total += curr_val
            else:
                total += curr_val
        return total

cases = [
    {
        'input':  "III",
        'solution': 3
    },
    {
        'input': "LVIII",
        'solution': 58
    },
    {
        'input': "MCMXCIV",
        'solution': 1994
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
        answer = Solution().romanToInt(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 