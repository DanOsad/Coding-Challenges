#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution(object):
    # This solution beats 90.99% in runtime
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if needle == haystack[i:i+len(needle)]:
                    return i
            continue
        return -1

    # This method beat 70.99% in runtime
    # def strStr(self, haystack, needle):
    #     inds = [ i for i, item in enumerate(haystack) if haystack[i] == needle[0] ] 
    #     for i in inds:
    #         if needle == haystack[i:i+len(needle)]:
    #             return i
    #     return -1


cases = [
    {
        'input':  ["sadbutsad", "sad"],
        'solution': 0
    },
    {
        'input': ["leetcode", "leeto"],
        'solution': -1
    },
    {
        'input': ["hello", "ll"],
        'solution': 2
    },
    {
        'input': ["mississippi", "issip"],
        'solution': 4
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
        # print(f'Testing Case {i}')
        answer = Solution().strStr(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 