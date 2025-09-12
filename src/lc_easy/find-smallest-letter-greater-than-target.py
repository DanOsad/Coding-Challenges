# https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        def get_lexographical_value(letter: str):
            alphabet = "abcdefghijklmnopqrstuvxyz"
            alpha_hash = {char: ind for ind, char in enumerate(alphabet)}

            return alpha_hash[letter]

        lexicographically_greater = letters[0]
        target_lex_value = get_lexographical_value(target)
        
        if target not in letters:
            return lexicographically_greater

        hi = len(letters) - 1
        lo = 0

        iteration = 0

        while hi >= lo:
            iteration += 1
            print(f'Iteration {iteration}: hi = {hi}, lo = {lo}')
            mid = (lo + ((lo - hi) // 2))
            # if value of letter at MID position is > than value of target
                # 
            mid_letter = letters[mid]
            mid_lex_value = get_lexographical_value(mid_letter)
            if mid_lex_value >= target_lex_value:
                hi = mid - 1
            elif mid_lex_value == target_lex_value:
                lo = mid
            else:
                lexicographically_greater = mid_letter
        print(f'Returning: {lexicographically_greater}')
        return lexicographically_greater



cases = [
    {
        'input':  [["c","f","j"], "a"],
        'solution': "c"
    },
    {
        'input': [["c","f","j"], "c"],
        'solution': "f"
    },
    {
        'input': [["x","x","y","y"], "z"],
        'solution': "x"
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