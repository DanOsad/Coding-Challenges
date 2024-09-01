# https://leetcode.com/problems/merge-strings-alternately

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # First try
        longer_word = word2 if len(word2) > len(word1) else word1
        r = ''
        for i in range(len(longer_word)):
            if i < len(word1):
                r += word1[i]
            if i < len(word2):
                r += word2[i]
        
        return r

        # Optimized
        result = []
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        result.extend([word1[min_length:], word2[min_length:]])
        return "".join(result)
    
cases = [
    {
        'input':  ["abc", "pqr"],
        'solution': "apbqcr"
    },
    {
        'input': ["ab", "pqrs"],
        'solution': "apbqrs"
    },
    {
        'input': ["abcd", "pq"],
        'solution': "apbqcd"
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
        answer = Solution().mergeAlternately(case['input'][0], case['input'][1])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

if __name__ == "__main__":
    test() 