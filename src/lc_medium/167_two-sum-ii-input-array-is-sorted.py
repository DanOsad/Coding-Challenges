# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i <= j:
            if target - numbers[j] == numbers[i]:
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i+1,j+1]

cases = [
    {
        'input': ([2, 7, 11, 15], 9),
        'solution': [1, 2]
    },
    {
        'input': ([2, 3, 4], 6),
        'solution': [1, 3]
    },
    {
        'input': ([-1, 0], -1),
        'solution': [1, 2]
    },
    {
        'input': ([5,25,75], 100),
        'solution': [2,3]
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().twoSum
    }
)
test_suite.run_tests()