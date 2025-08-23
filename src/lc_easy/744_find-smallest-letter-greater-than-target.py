# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Naive solution
        # all_letters = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        # lex = {c: i for i, c in enumerate(all_letters)}
        # remaining_letters = {i:c for i,c in enumerate(all_letters) if i > lex[target]}
        # for letter in letters:
        #     if letter in remaining_letters.values():
        #         return letter
        # return letters[0]
    
        # Optimized Solution
        all_letters = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        lex = {c: i for i, c in enumerate(all_letters)}
        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if lex[letters[mid]] > lex[target]:
                hi = mid - 1
            elif lex[letters[mid]] <= lex[target]:
                lo = mid + 1
        return letters[lo] if lo < len(letters) else letters[0]
            
cases = [
    {
        'input': [["c","f","j"], "a"],
        'solution': 'c'
    },
    {
        'input': [["c","f","j"], "c"],
        'solution': 'f'
    },
    {
        'input': [["x","x","y","y"], "z"],
        'solution': 'x'
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().nextGreatestLetter
    }
)
test_suite.run_tests()