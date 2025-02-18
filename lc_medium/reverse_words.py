# 151 - https://leetcode.com/problems/reverse-words-in-a-string

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        word_list = [word.strip() for word in s.split()]
        for _ in range(len(word_list)):
            word_list.insert(i, word_list.pop(-1))
            i += 1
        return " ".join(word_list)

cases = [
    {
        'input':  "the sky is blue",
        'solution': "blue is sky the"
    },
    {
        'input': "  hello world  ",
        'solution': "world hello"
    },
    {
        'input': "a good   example",
        'solution': "example good a"
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
        answer = Solution().reverseWords(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 