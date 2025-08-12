# 49 https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        char_maps = {}

        for word in strs:
            s = tuple(sorted(word))
            if s not in char_maps:
                char_maps[s] = [word]
            elif s in char_maps:
                char_maps[s].append(word)
        return list(char_maps.values())


cases = [ 
    {
        'input':  [""],
        'solution': [[""]]
    },
    {
        'input': ["a"],
        'solution': [["a"]]
    },
    {
        'input': ["eat","tea","tan","ate","nat","bat"],
        'solution': [["bat"],["nat","tan"],["ate","eat","tea"]]
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
        answer = Solution().groupAnagrams(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 