# 394 https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        r = ""

        i = 0
        j = 0
        multiplier = 1

        while i < len(s):
            if s[i].isnumeric():
                print(f'Got multiplier {s[i]}')
                multiplier = int(s[i])
                i += 2
                j = i
                to_add = ""
                while s[j] not in ['[',']']:
                    print(f'Adding {s[j]} to multiplier')
                    to_add += s[j]
                    j += 1
                print(f'Multiplier = {multiplier}')
                for k in range(multiplier):
                    print(k, to_add)
                    r += to_add
                # r += multiplier * to_add
                multiplier = 1
            elif s[i] not in ['[',']']:
                r += s[i]
            i += 1
            print(f'State of r: {r}')

        return r

cases = [ 
    {
        'input':  "3[a]2[bc]",
        'solution': "aaabcbc"
    },
    {
        'input': "3[a2[c]]",
        'solution': "accaccacc"
    },
    {
        'input': "2[abc]3[cd]ef",
        'solution': "abcabccdcdcdef"
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
        answer = Solution().decodeString(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 