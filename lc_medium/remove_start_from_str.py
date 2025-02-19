#2390 https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def largestAltitude(self, s: str) -> str:
        # NAIVE APPROACH #
        # i=0
        # s = [c for c in s]
        # print(len(s), s)
        # while i < len(s[:]):
        #     print(s[i])
        #     if s[i] == "*":
        #         print(f'Removing {s[i]} & {s[i-1]}')
        #         s.pop(i)
        #         s.pop(i-1)
        #         print(s)
        #         i -= 1
        #     else:
        #         i += 1
        #         # ret += s[i]
        # return "".join(s)
    
        # OPTIMIZED APPROACH #
        r = []
        i = 0

        for i in range(len(s)):
            if s[i] == "*":
                r.pop()
            else:
                r.append(s[i])
            i+=1

        return "".join(r)
    
cases = [
    {
        'input':  "leet**cod*e",
        'solution': "lecoe"
    },
    {
        'input': "erase*****",
        'solution': ""
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
        answer = Solution().largestAltitude(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 